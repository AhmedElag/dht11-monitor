import RPi.GPIO as GPIO
import time
import Adafruit_DHT # Import the Adafruit DHT library for DHT11 sensor

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4   # BCM gpio 4 for DHT11 DATA

GREEN_LED_PIN= 20 # gpiop 20 for green LED
RED_LED_PIN= 21 # gpio 21 for red LED
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(RED_LED_PIN, GPIO.OUT)

# constants
HUMIDITY_THRESHOLD = 60.0  # 60% threshold for humidity
TEMP_THRESHOLD     = 30.0  # 30 degrees Celsius threshold for temperature

try:
    while True:
        # Read from DHT11
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None: # make sure we are getting readings first
            # Check conditions
            if temperature > TEMP_THRESHOLD or humidity > HUMIDITY_THRESHOLD: # if either or are above threshold
                # Turn on RED LED, turn off GREEN LED
                GPIO.output(RED_LED_PIN, True)
                GPIO.output(GREEN_LED_PIN, False)
                print("WARNING temp or humidity too hot")
            else: # unbder threshold
                # Turn on GREEN LED, turn off RED LED
                GPIO.output(GREEN_LED_PIN, True)
                GPIO.output(RED_LED_PIN, False)
                # Print normal readings
                print(f"Temp: {temperature:.1f}°C  |  Humidity: {humidity:.1f}%")

        else:
            print("Failed to retrieve data from DHT11 sensor.")

        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting script")

finally:
    GPIO.cleanup()


