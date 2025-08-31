import socket
import threading
import random
import time

HOST = '0.0.0.0'
PORT = 5000

clients = {}      # name -> socket
players = {}      # name -> {'HP':100, 'Attack':int}
lock = threading.Lock()

def broadcast(msg):
    with lock:
        for c in clients.values():
            try:
                c.sendall((msg + "\n").encode())
            except:
                pass

def broadcast_status():
    status = "=== 玩家狀態 ===\n"
    for name, info in players.items():
        status += f"{name}: HP={info['HP']}, 攻擊={info['Attack']}\n"
    broadcast(status)

def init_player(client):
    client.send("請輸入你的名字: ".encode())
    name = client.recv(1024).decode().strip()
    with lock:
        clients[name] = client
        players[name] = {'HP':100, 'Attack':random.randint(10,20)}
    broadcast(f"👋 {name} 加入遊戲！")
    broadcast_status()
    return name

def turn_game():
    while len(players) == 2:  # 只玩兩個人
        for name in list(players.keys()):
            client = clients[name]
            broadcast(f"➡️ 輪到 {name} 行動！輸入 attack <玩家> 或 pass")
            msg = client.recv(1024).decode().strip()
            if msg.lower() == "pass":
                client.send("你選擇跳過回合\n".encode())
            elif msg.lower().startswith("attack"):
                parts = msg.split()
                if len(parts) == 2 and parts[1] in players and parts[1] != name:
                    target = parts[1]
                    dmg = players[name]['Attack']
                    players[target]['HP'] -= dmg
                    broadcast(f"{name} 攻擊 {target} 造成 {dmg} 傷害！")
                    if players[target]['HP'] <= 0:
                        broadcast(f"💀 {target} 被淘汰！")
                        clients[target].close()
                        del clients[target]
                        del players[target]
                else:
                    client.send("無效目標！\n".encode())
            broadcast_status()
            if len(players) <= 1:
                winner = list(players.keys())[0]
                broadcast(f"🏆 {winner} 勝利！遊戲結束")
                return

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)
    print(f"伺服器啟動 (PORT {PORT}) ...")

    # 先接受兩個玩家連線
    connections = []
    for _ in range(2):
        client, addr = server.accept()
        connections.append(client)

    # 同步初始化兩個玩家
    names = []
    for client in connections:
        name = init_player(client)
        names.append(name)

    print("兩個玩家已加入，遊戲開始！")
    turn_game()

if __name__ == "__main__":
    main()