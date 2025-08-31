import socket

HOST = '127.0.0.1'  # 本機
PORT = 5000         # 隨意 > 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))   # 綁定 IP + PORT
    s.listen()             # 開始監聽
    print("等待客戶端連線...")
    conn, addr = s.accept()  # 接受連線
    with conn:
        print("連線來自：", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = data.decode()
            print("收到:", msg)
            name = msg.split("my name is")[-1].strip()
            reply = f"Hello {name}"
            conn.sendall(reply.encode())
