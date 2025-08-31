import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("伺服器啟動，等待客戶端連線...")

    while True:  # 一直等待新的 Client
        conn, addr = s.accept()
        with conn:
            print("連線來自：", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    print("客戶端斷線:", addr)
                    break
                msg = data.decode()
                print("收到:", msg)

                if "my name is" in msg:
                    name = msg.split("my name is")[-1].strip()
                    reply = f"Hello {name}"
                else:
                    reply = f"your msg :  {msg}"
                conn.sendall(reply.encode())
