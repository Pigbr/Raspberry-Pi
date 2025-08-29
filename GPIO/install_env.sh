#!/bin/bash
# Raspberry Pi GPIO 開發環境安裝腳本

# 建立虛擬環境
python3 -m venv ~/myenv
source ~/myenv/bin/activate

# 更新系統
sudo apt update
sudo apt install -y build-essential python3-dev python3-pip libgpiod2 pigpio python3-pigpio

# 安裝 Python 套件
pip install --upgrade pip
pip install RPi.GPIO gpiozero pigpio adafruit-blinka adafruit-circuitpython-dht

# 啟動 pigpio 服務（舵機會需要）
sudo systemctl enable pigpiod
sudo systemctl start pigpiod

echo "======================================"
echo "✅ 安裝完成！"
echo "使用方法："
echo "  source ~/myenv/bin/activate   # 啟動虛擬環境"
echo "  python your_program.py        # 執行你的程式"
echo "======================================"
