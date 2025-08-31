import socket

HOST = '127.0.0.1'  # 例如 '192.168.1.100'
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(s.recv(1024).decode())
    while True:
        cmd = input("> ").strip()
        s.sendall(cmd.encode())
        print(s.recv(1024).decode())
