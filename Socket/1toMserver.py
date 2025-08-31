import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def handle_client(conn, addr):
    """處理單一客戶端連線"""
    print("連線來自：", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                print("客戶端斷線:", addr)
                break
            msg = data.decode()
            print(f"[{addr}] 收到: {msg}")

            if "my name is" in msg:
                name = msg.split("my name is")[-1].strip()
                reply = f"Hello {name}"
            else:
                reply = f"your msg : {msg}"
            conn.sendall(reply.encode())

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("伺服器啟動，等待客戶端連線...")

        while True:
            conn, addr = s.accept()
            # 每個客戶端交給一個新 thread 處理
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.daemon = True  # 設為 daemon 避免阻塞程式結束
            thread.start()
            print(f"目前活躍連線數: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()