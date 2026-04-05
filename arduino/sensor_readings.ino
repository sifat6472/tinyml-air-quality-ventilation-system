
#include <DHT.h>
#include <Servo.h>

#define DHTPIN 2
#define DHTTYPE DHT11
#define MQ135_PIN A0
#define SERVO_PIN 9   // PWM pin

DHT dht(DHTPIN, DHTTYPE);
Servo windowServo;

void setup() {
  Serial.begin(9600);
  dht.begin();

  windowServo.attach(SERVO_PIN);
  windowServo.write(0);  // start CLOSED

  delay(2000);
}

void loop() {
  // ----------------------
  // SENSOR READINGS
  // ----------------------
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  int gas = analogRead(MQ135_PIN);

  // ----------------------
  // SEND DATA TO PI
  // ----------------------
  Serial.print(temperature);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.println(gas);

  // ----------------------
  // RECEIVE COMMAND FROM PI
  // ----------------------
  if (Serial.available()) {
    char cmd = Serial.read();

    if (cmd == 'G') {
      windowServo.write(0);    // closed
    }
    else if (cmd == 'M') {
      windowServo.write(50);   // half open
    }
    else if (cmd == 'P') {
      windowServo.write(150);   // full open
    }
  }

  delay(2000); // 1 sample every 2 sec
}

