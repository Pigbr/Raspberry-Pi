#!/bin/bash
folder="$HOME/Desktop/today_project/Raspberry-Pi/Shell_Script"
for f in "$folder"/*.txt; do
    base=$(basename "$f" .txt)
    mv "$f" "$folder/${base}_submitted.txt"
done
echo "檔名修改完成！"
