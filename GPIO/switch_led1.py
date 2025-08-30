from gpiozero import LED

led = LED(18)

print("輸入 on 開燈, off 關燈, q 離開")

while True:
    cmd = input(">> ").strip().lower()
    if cmd == "on":
        led.on()
    elif cmd == "off":
        led.off()
    elif cmd == "q":
        led.off()
        print("Bye~")
        break
    else:
        print("指令無效，請輸入 on / off / q")