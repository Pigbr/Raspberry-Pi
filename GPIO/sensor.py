import adafruit_dht
import board
import time

dht_device = adafruit_dht.DHT11(board.D4)

try:
    temperature_c = dht_device.temperature
    humidity = dht_device.humidity
    print(f"{temperature_c},{humidity}\n")
except Exception as e:
    print("讀取失敗:", e)
finally:
    # 不管上面成功或失敗，都會執行這裡
    dht_device.exit()
    print("釋放 DHT11 資源")
