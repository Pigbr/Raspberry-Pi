#!/bin/sh
# 猜數字遊戲 (1~100)

# 產生隨機數字 (1-100)
target=$(shuf -i 1-100 -n 1)

echo "===== 猜數字遊戲 ====="
echo "我已經想好一個 1 到 100 的數字，來猜吧！"

while true
do
    printf "請輸入你的猜測: "
    read guess

    # 判斷是否為數字
    if ! echo "$guess" | grep -Eq '^[0-9]+$'; then
        echo "請輸入數字！"
        continue
    fi

    if [ "$guess" -eq "$target" ]; then
        echo "恭喜猜對了！答案是 $target"
        break
    elif [ "$guess" -gt "$target" ]; then
        echo "太大了 "
    else
        echo "太小了 "
    fi
done
