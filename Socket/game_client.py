import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break
            print("\n" + msg + "\n> ", end="")
        except:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    threading.Thread(target=receive_messages, args=(s,), daemon=True).start()
    name = input("請輸入你的名字: ")
    s.sendall(name.encode())

    while True:
        cmd = input("> ")
        s.sendall(cmd.encode())