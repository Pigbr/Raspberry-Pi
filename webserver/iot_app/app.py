from flask import Flask
from gpiozero import LED

led = LED(18)
app = Flask(__name__)

@app.route("/")
def index():
    return """
        <h1>Raspberry Pi IoT Web</h1>
        <a href='/led/on'>LED ON</a><br>
        <a href='/led/off'>LED OFF</a>
    """

@app.route("/led/on")
def led_on():
    led.on()
    return "LED is ON"

@app.route("/led/off")
def led_off():
    led.off()
    return "LED is OFF"

if __name__ == "__main__":
    app.run()
