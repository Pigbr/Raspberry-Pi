import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    name = input("請輸入你的名字: ")
    s.connect((HOST, PORT))
    message = f"Hello Server my name is {name}"
    s.sendall(message.encode())   # 用 .encode() 轉成 bytes
    data = s.recv(1024)
    print("伺服器回覆:", data.decode())


    while True:
        message = input("請輸入要傳給伺服器的訊息 (輸入 quit 離開): ")
        if message.lower() == "quit":
            print("斷開連線")
            break

        s.sendall(message.encode())
        data = s.recv(1024)
        print("伺服器回覆:", data.decode())
