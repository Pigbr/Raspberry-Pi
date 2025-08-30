from gpiozero import LED
from time import sleep

# 建立 LED
led = LED(18)

# 摩斯密碼字典
MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',  'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....', 'I': '..',   'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',   'N': '-.',   'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',  'S': '...',  'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',  'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---','3': '...--','4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..','9': '----.',
    ' ': ' '  # 空白當作單字間隔
}

# 基本時間單位 (秒)
DOT = 0.2      # 點
DASH = DOT*3   # 劃
LETTER_SPACE = DOT*3   # 字母之間
WORD_SPACE = DOT*7     # 單字之間

def blink_dot():
    print('.', end='', flush=True)
    led.on()
    sleep(DOT)
    led.off()
    sleep(DOT)  

def blink_dash():
    print('-', end='', flush=True)
    led.on()
    sleep(DASH)
    led.off()
    sleep(DOT)  

def morse(text):
    text = text.upper()
    for char in text:
        if char not in MORSE_CODE:
            continue
        code = MORSE_CODE[char]
        if code == ' ':
            print('      ', end='', flush=True)
            sleep(WORD_SPACE)  # 單字間隔
        else:
            for symbol in code:
                if symbol == '.':
                    blink_dot()
                elif symbol == '-':
                    blink_dash()
            sleep(LETTER_SPACE)  # 字母間隔

# 主程式
if __name__ == "__main__":
    msg = input("請輸入要用摩斯碼顯示的文字: ")
    print(f"正在輸出: {msg}")
    morse(msg)
    print("\n顯示完成！")
