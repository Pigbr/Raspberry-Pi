#!/bin/bash

logfile="$(pwd)/mylog.txt"

read -p "輸入今天的心得: " note

echo "$(date '+%Y-%m-%d %H:%M:%S') - $note" >> $logfile
echo "已紀錄！"
