import serial
import time

from gpiozero import PWMOutputDevice

# OLED
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# ----------------------
# CONFIG
# ----------------------
SERIAL_PORT = "/dev/ttyACM0"
BAUD_RATE = 9600
FAN_PIN = 17
MAX_RPM = 3000

# ----------------------
def classify_air(air):
    if air < 45:
        return "good"
    elif air < 60:
        return "moderate"
    else:
        return "poor"

def rpm_from_pwm(pwm_value):
    return int(pwm_value * MAX_RPM)

# ----------------------
def main():
    ser = None
    fan = None

    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)

        # OLED
        i2c = busio.I2C(board.SCL, board.SDA)
        oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
        oled.fill(0)
        oled.show()

        image = Image.new("1", (128, 64))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        fan = PWMOutputDevice(FAN_PIN)
        fan.value = 0.0

        while True:
            line = ser.readline().decode().strip()
            if not line:
                continue

            temp, hum, air = map(float, line.split(","))

            quality = classify_air(air)

            if quality == "good":
                fan.value = 0.0
                window = "CLOSED"
                ser.write(b'G')

            elif quality == "moderate":
                fan.value = 0.5
                window = "PARTIAL"
                ser.write(b'M')

            elif quality == "poor":
                fan.value = 1.0
                window = "FULL"
                ser.write(b'P')

            rpm = rpm_from_pwm(fan.value)
          
            draw.rectangle((0, 0, 128, 64), fill=0)
            draw.text((0, 0),  f"T:{temp:.1f}C H:{hum:.1f}%", font=font, fill=255)
            draw.text((0, 15), f"AQ:{air:.0f}", font=font, fill=255)
            draw.text((0, 27), f"Air: {quality.upper()}", font=font, fill=255)
            draw.text((0, 40), f"Fan:{rpm} RPM", font=font, fill=255)
            draw.text((0, 52), f"{window}", font=font, fill=255)


            oled.image(image)
            oled.show()

            time.sleep(0.3)

    except KeyboardInterrupt:
        print("Stopped")

    finally:
        if fan:
            fan.off()
        if ser and ser.is_open:
            ser.close()


if __name__ == "__main__":
    main()
