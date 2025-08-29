#!/bin/bash

# 取得參數
option=$1

case $option in
    1)
        # 原本的測試檔案
        touch photo1.jpg photo2.png
        touch report.pdf notes.txt
        touch backup.zip archive.tar.gz
        touch movie.mp4 music.mp3
        echo "創建完成：原本測試檔案"
        ;;
    2)
        # 創 10 個 txt 檔案
        for i in {1..10}; do
            touch "file$i.txt"
        done
        echo "創建完成：10 個 txt 檔案"
        ;;
    *)
        echo "請輸入參數：1 或 2"
        ;;
esac

