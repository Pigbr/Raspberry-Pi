import socket
import threading
from gpiozero import LED

HOST = '0.0.0.0'
PORT = 5001

led = LED(18)  # GPIO18 接 LED

def handle_client(client):
    client.send("控制 LED: 輸入 on 或 off\n".encode())
    while True:
        try:
            msg = client.recv(1024).decode().strip().lower()
            if not msg:
                break
            if msg == "on":
                led.on()
                client.send("LED 已經亮起\n".encode())
            elif msg == "off":
                led.off()
                client.send("LED 已經熄滅\n".encode())
            else:
                client.send("無效指令，請輸入 on 或 off\n".encode())
        except:
            break
    client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"LED 控制伺服器啟動，PORT {PORT} ...")
    while True:
        client, addr = server.accept()
        print(f"連線來自: {addr}")
        threading.Thread(target=handle_client, args=(client,), daemon=True).start()

if __name__ == "__main__":
    main()
