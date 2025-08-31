import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def receive(sock):
    """接收伺服器的訊息"""
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print("\n" + data.decode() + "\n> ", end="")
        except:
            break

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("已連線到聊天室！輸入訊息開始聊天 (Ctrl+C 離開)")

        # 開啟接收訊息的 thread
        threading.Thread(target=receive, args=(s,), daemon=True).start()

        while True:
            msg = input("> ")
            if msg.lower() == "exit":
                break
            s.sendall(msg.encode())

if __name__ == "__main__":
    main()
