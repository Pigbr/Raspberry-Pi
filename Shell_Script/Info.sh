#!/bin/bash
echo "=== 系統資訊 ==="
echo "CPU 使用率:"
top -bn1 | grep "Cpu(s)"
echo "記憶體使用狀態:"
free -h
echo "磁碟使用狀態:"
df -h
