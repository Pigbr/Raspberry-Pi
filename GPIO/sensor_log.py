import adafruit_dht
import board
import time
from datetime import datetime

dht_device = adafruit_dht.DHT11(board.D4)

try:
    while True:
        try:
            temperature_c = dht_device.temperature
            humidity = dht_device.humidity
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line = f"{now},{temperature_c},{humidity}"
            
            print(line)  # 印在螢幕上
            # 寫入 txt 檔
            with open("dht11_log.txt", "a") as f:
                f.write(line + "\n")
                
        except RuntimeError as e:
            # DHT11 偶爾讀失敗，重試
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - 讀取失敗: {e}")
        except Exception as e:
            # 其他錯誤
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - 發生錯誤: {e}")
        
        time.sleep(2)  # 每2秒讀取一次

finally:
    dht_device.exit()
    print("釋放 DHT11 資源")
