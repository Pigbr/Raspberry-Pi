from flask import Flask, render_template_string, request, jsonify
import pigpio
import adafruit_dht
import board
import time

app = Flask(__name__)

# GPIO 設定
LED_PIN = 18
SERVO_PIN = 17
DHT_PIN = board.D4  # 使用 board.Dx

pi = pigpio.pi()
pi.set_mode(LED_PIN, pigpio.OUTPUT)
pi.set_mode(SERVO_PIN, pigpio.OUTPUT)

# 建立 DHT11 實例
dht_device = adafruit_dht.DHT11(DHT_PIN)

# HTML 網頁模板
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Raspberry Pi IoT Panel</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
    <script>
    // 每秒更新 DHT11
    async function updateDHT() {
        const response = await fetch('/dht');
        const data = await response.json();
        document.getElementById('temperature').innerText = data.temperature + ' °C';
        document.getElementById('humidity').innerText = data.humidity + ' %';
    }
    setInterval(updateDHT, 1000);

    // 控制 SG90 任意角度
    async function setServo() {
        const angle = document.getElementById('servoRange').value;
        await fetch('/servo_angle?angle=' + angle);
        document.getElementById('servoValue').innerText = angle + '°';
    }
    </script>
</head>
<body class="bg-light">
<div class="container py-4">
    <h1 class="mb-4 text-center">Raspberry Pi IoT Control Panel</h1>

    <div class="card mb-3">
        <div class="card-header">LED 控制</div>
        <div class="card-body">
            <a href="/led/on" class="btn btn-success">LED ON</a>
            <a href="/led/off" class="btn btn-danger">LED OFF</a>
        </div>
    </div>

    <div class="card mb-3">
        <div class="card-header">SG90 舵機控制</div>
        <div class="card-body">
            <label for="servoRange" class="form-label">角度: <span id="servoValue">90°</span></label>
            <input type="range" class="form-range" id="servoRange" min="0" max="180" value="90" oninput="setServo()">
        </div>
    </div>

    <div class="card mb-3">
        <div class="card-header">DHT11 感測器</div>
        <div class="card-body">
            <p>溫度: <span id="temperature">讀取中...</span></p>
            <p>濕度: <span id="humidity">讀取中...</span></p>
        </div>
    </div>
</div>
</body>
</html>
"""

# 網頁首頁
@app.route("/")
def index():
    return render_template_string(HTML)

# LED 控制
@app.route("/led/<state>")
def led_control(state):
    if state == "on":
        pi.write(LED_PIN, 1)
    elif state == "off":
        pi.write(LED_PIN, 0)
    return "LED " + state.upper() + ". <a href='/'>回首頁</a>"

# SG90 任意角度控制
@app.route("/servo_angle")
def servo_angle():
    angle = int(request.args.get("angle", 90))
    pulse = 500 + (angle / 180) * 2000  # 500~2500 μs 對應 0~180°
    pi.set_servo_pulsewidth(SERVO_PIN, pulse)
    return jsonify({"angle": angle})

# DHT11 即時讀取
@app.route("/dht")
def dht():
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        if temperature is None or humidity is None:
            temperature = humidity = "讀取失敗"
    except Exception as e:
        temperature = humidity = "讀取失敗"
    return jsonify({"temperature": temperature, "humidity": humidity})

# 停止 GPIO
@app.route("/shutdown")
def shutdown():
    pi.write(LED_PIN, 0)
    pi.set_servo_pulsewidth(SERVO_PIN, 0)
    pi.stop()
    try:
        dht_device.exit()
    except:
        pass
    return "GPIO 已清理，Flask 可關閉"

if __name__ == "__main__":
    app.run()
