from gpiozero import LED
from time import sleep

led = LED(18)   # GPIO18 接 LED

while True:
    led.on()    # 亮
    sleep(5)
    led.off()   # 滅
    sleep(5)
