# 🌿 TinyML-Based Indoor Air Quality Prediction and Ventilation Control System

> 🚀 TinyML + Embedded Systems + Automation Project

## 📌 Overview
This project is an intelligent air quality monitoring system that uses TinyML and embedded systems to automatically control ventilation based on real-time environmental conditions.

The system monitors:
- Temperature
- Humidity
- Air Quality (MQ-135)

Based on the sensor data, a Raspberry Pi runs a TinyML model to classify air quality into:
- GOOD
- MODERATE
- POOR

---

## 🎥 Demo Video

👉 [Watch the Full Project Demo]([PASTE_YOUR_GOOGLE_DRIVE_LINK_HERE](https://drive.google.com/file/d/1MROwH9SBrpOD_QHrbicEzA3MD9c_ZuSn/view))

---

## ⚙️ System Workflow

1. Arduino reads sensor data (DHT11 + MQ135)
2. Sends data to Raspberry Pi via Serial Communication
3. Raspberry Pi runs TinyML model (Edge Impulse)
4. Based on prediction:
   - Controls Fan speed (PWM)
   - Sends signal back to Arduino
5. Arduino controls Servo Motor (window opening)
6. OLED displays all real-time data

---

## 🔁 Control Logic

| Condition | Fan Speed | RPM | Servo Angle | Window |
|----------|----------|-----|------------|--------|
| GOOD     | OFF      | 0   | 0°         | Closed |
| MODERATE | Medium   | 1500| 50°        | Partial Open |
| POOR     | Full     | 3000| 150°       | Fully Open |

---

## 🧠 Machine Learning

- Platform: Edge Impulse
- Input: Temperature, Humidity, Air Quality
- Output: Good / Moderate / Poor

---

## 📊 Results

### 🔴 Poor Condition
- Temperature: 40°C  
- Humidity: 20%  
- Air Quality: 456  
- Prediction: **POOR**  
- Fan: **3000 RPM (Full Speed)**  
- Servo: **150° (Fully Open Window)**  

### 🟡 Moderate Condition
- Temperature: 30°C  
- Humidity: 61%  
- Air Quality: 330  
- Prediction: **MODERATE**  
- Fan: **1500 RPM (Medium Speed)**  
- Servo: **50° (Partially Open Window)**  

### 🟢 Good Condition
- Temperature: 27°C  
- Humidity: 70%  
- Air Quality: 120  
- Prediction: **GOOD**  
- Fan: **OFF (0 RPM)**  
- Servo: **0° (Window Closed)**  

---

## 🔌 Hardware Components

- Raspberry Pi 5  
- Arduino Uno  
- DHT11 Sensor  
- MQ-135 Gas Sensor  
- SG90 Servo Motor  
- 5V DC Fan  
- OLED Display (SSD1306)  
- NPN Transistor  
- 1kΩ Resistor  
- Breadboard & Jumper Wires  

---

## 🔗 Communication

- Arduino ↔ Raspberry Pi → Serial (UART)  
- Raspberry Pi → OLED → I2C  
- Raspberry Pi → Fan → PWM GPIO  
- Raspberry Pi → Arduino → Serial  
- Arduino → Servo → PWM  

---

## 📷 Project Images

![Sensor](images/sensorsjpg)  
![Fan](images/fan.jpg)   
![Servo](images/servo.jpg)  
![OLED](images/oled.jpg)  
![System](images/system.jpg)  

---

## 🚀 How to Run

### Raspberry Pi
pip install -r requirements.txt
python3 ml_code.py


### Arduino
Upload `sensor_readings.ino` using Arduino IDE.

---

## 👨‍💻 Team Members

- 👤 [Member 1](https://github.com/username1) — System Integration  
- 👤 [Member 2](https://github.com/username2) — Arduino & Sensors  
- 👤 [Member 3](https://github.com/username3) — Raspberry Pi & ML  
- 👤 [Member 4](https://github.com/username4) — Documentation & Testing  

---

## 🔮 Future Improvements

- Add PIR sensor for energy saving  
- Mobile app monitoring  
- Wireless communication (WiFi/Bluetooth)  
- Improve ML accuracy  

---

## 📜 License
This project is licensed under the MIT License.
