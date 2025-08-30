import RPi.GPIO as GPIO
import time

LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # 亮
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)   # 滅
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()