import time
import board
import adafruit_dht
import RPi.GPIO as GPIO
import threading

# === 硬體設定 ===
LED_PIN = 18
SERVO_PIN = 17
DHT_PIN = board.D4  # DHT11 接腳

# 初始化 GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Servo 使用 PWM (50Hz)
servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)

# 初始化 DHT11
dht_device = adafruit_dht.DHT11(DHT_PIN)

# === 控制變數 ===
servo_active = False  # Thread 控制開關
servo_thread = None

# === 工具函式 ===
def blink_led(times=3, interval=0.3):
    """LED 閃爍指定次數"""
    for _ in range(times):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(interval)

def set_servo_angle(angle):
    """設定 Servo 角度 (0 ~ 180)"""
    duty = 2 + (angle / 18)  # 角度轉 PWM duty cycle
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

def servo_loop():
    """舵機持續擺動 0 -> 180 -> 0"""
    while servo_active:
        for angle in [0, 180, 0]:
            if not servo_active:
                break
            set_servo_angle(angle)

# === 系統啟動 ===
print("系統初始化中...")
blink_led(3)
print("✅ 初始化完成，開始運作...")

try:
    while True:
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity

            if temperature is not None and humidity is not None:
                print(f"🌡 溫度: {temperature}°C, 💧 濕度: {humidity}%")

                if temperature > 29:
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    if not servo_active:
                        # 啟動舵機 thread
                        servo_active = True
                        servo_thread = threading.Thread(target=servo_loop)
                        servo_thread.start()
                else:
                    GPIO.output(LED_PIN, GPIO.LOW)
                    if servo_active:
                        # 停止舵機 thread
                        servo_active = False
                        servo_thread.join()
                        set_servo_angle(0)  # 歸位

            else:
                print("⚠️ 感測器讀取失敗")

        except Exception as e:
            print("讀取錯誤:", e)

        time.sleep(2)

except KeyboardInterrupt:
    print("👋 程式結束")

finally:
    servo_active = False
    if servo_thread is not None:
        servo_thread.join()
    dht_device.exit()
    servo.stop()
    GPIO.cleanup()
