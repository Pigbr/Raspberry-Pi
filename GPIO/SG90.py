import pigpio
import time

# 連線到 pigpiod
pi = pigpio.pi()
if not pi.connected:
    exit("無法連線到 pigpiod")

servo_pin = 17  # SG90 信號線接 GPIO17

# 角度轉微秒函式 (SG90: 0°~180° 對應 500~2500us)
def set_angle(angle):
    pulsewidth = 500 + (angle / 180.0) * 2000  # 0°->500us, 180°->2500us
    pi.set_servo_pulsewidth(servo_pin, pulsewidth)
    time.sleep(0.5)

try:
    while True:
        for angle in [0, 45, 90, 135, 180, 90, 45, 0]:
            print(f"轉到角度: {angle}°")
            set_angle(angle)
            time.sleep(1)

except KeyboardInterrupt:
    print("程式結束")

finally:
    pi.set_servo_pulsewidth(servo_pin, 0)  # 停止 PWM
    pi.stop()  # 關閉 pigpio 連線
    print("釋放 GPIO")
