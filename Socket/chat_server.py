import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

clients = []  # 保存所有連線的 client socket
lock = threading.Lock()

def broadcast(message, conn):
    """廣播訊息給所有客戶端"""
    with lock:
        for client in clients:
            if client != conn:  # 不回傳給自己
                try:
                    client.sendall(message)
                except:
                    clients.remove(client)

def handle_client(conn, addr):
    print(f"連線來自: {addr}")
    with lock:
        clients.append(conn)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = f"[{addr}] {data.decode()}"
            print(msg)
            broadcast(msg.encode(), conn)
    except:
        pass
    finally:
        with lock:
            clients.remove(conn)
        conn.close()
        print(f"客戶端斷線: {addr}")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("聊天室伺服器啟動，等待連線...")

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    start_server()
