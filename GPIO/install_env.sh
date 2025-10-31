#!/bin/bash
# ======================================
# Raspberry Pi GPIO 開發環境安裝腳本
# 支援舵機 (pigpiod daemon) Trixie 系統
# ======================================

set -e  # 發生錯誤時停止

# 建立 Python 虛擬環境
echo "🔧 建立 Python 虛擬環境..."
python3 -m venv ~/myenv
source ~/myenv/bin/activate

# 更新系統與安裝依賴
echo "🔄 更新系統並安裝必要套件..."
sudo apt update
sudo apt install -y \
    build-essential \
    python3-dev \
    python3-pip \
    python3-gpiozero \
    pigpio-tools \
    python3-pigpio \
    libgpiod-dev \
    gpiod \
    git

# 安裝 Python 套件
echo "📦 安裝 Python 套件..."
pip install --upgrade pip
pip install RPi.GPIO gpiozero pigpio adafruit-blinka adafruit-circuitpython-dht

# 檢查 pigpiod 是否存在
if ! command -v pigpiod >/dev/null 2>&1; then
    echo "⚠️ pigpiod 不存在，從原始碼編譯安裝..."
    cd /tmp
    git clone https://github.com/joan2937/pigpio.git
    cd pigpio
    make
    sudo make install
fi

# 啟動 pigpio daemon
echo "🚀 啟動 pigpio 服務..."
sudo pkill pigpiod 2>/dev/null || true
sudo pigpiod &
sleep 1

# 完成提示
echo "======================================"
echo "✅ Raspberry Pi GPIO 開發環境安裝完成！"
echo ""
echo "使用方法："
echo "  source ~/myenv/bin/activate   # 啟動虛擬環境"
echo "  python your_program.py        # 執行你的程式"
echo "======================================"
