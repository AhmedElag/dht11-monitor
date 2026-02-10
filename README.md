# DHT11 Monitor (Raspberry Pi)

## Overview
This project implements a temperature and humidity monitoring system using a **DHT11 sensor** connected to a **Raspberry Pi**. The system continuously reads environmental data and provides visual feedback using LEDs based on predefined threshold values.

A demo of the system running on hardware is available here:  
https://www.youtube.com/shorts/_4LwvI01vus

---

## Functionality
- Reads temperature (°C) and humidity (%) from a DHT11 sensor once per second
- Compares readings against fixed threshold values
- Activates LEDs to indicate normal or warning conditions
- Prints live sensor readings and status messages to the terminal

### Alert Logic
- **Red LED ON**  
  Triggered when:
  - Temperature > 30°C **OR**
  - Humidity > 60%
- **Green LED ON**  
  Triggered when both values are within safe limits

---

## Hardware Components
- Raspberry Pi
- DHT11 temperature and humidity sensor
- Red LED + 220Ω resistor
- Green LED + 220Ω resistor
- 10 kΩ pull-up resistor (required for some DHT11 modules)
- Breadboard and jumper wires

---

## GPIO Wiring (BCM Mode)

### DHT11 Sensor
- VCC → 3.3V
- DATA → GPIO4
- GND → GND
- 10 kΩ resistor between DATA and VCC

### LEDs
**Green LED**
- GPIO20 → 220Ω resistor → LED → GND

**Red LED**
- GPIO21 → 220Ω resistor → LED → GND

---
### Author
Ahmed Elag  


*This project was originally completed as part of a university course and is shared for educational and portfolio purposes.*
## Software Requirements
- Raspberry Pi OS
- Python 3
- Libraries:
  - `RPi.GPIO`
  - `Adafruit_DHT`

### Install Dependencies
```bash
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install Adafruit_DHT
