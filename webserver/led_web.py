from flask import Flask
from gpiozero import LED

app = Flask(__name__)
led = LED(18)

@app.route("/")
def home():
    return "控制 LED: /on 開燈, /off 關燈"

@app.route("/on")
def turn_on():
    led.on()
    return "LED ON"

@app.route("/off")
def turn_off():
    led.off()
    return "LED OFF"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
