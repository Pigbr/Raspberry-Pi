#!/bin/bash
folder="$(pwd)"
success=true

for f in "$folder"/*.txt; do
    # 如果沒有匹配到任何 .txt，跳出迴圈
    [[ -e "$f" ]] || { echo "找不到 .txt 檔案"; success=false; break; }

    base=$(basename "$f" .txt)
    if ! mv "$f" "$folder/${base}_submitted.txt"; then
        echo "重新命名失敗：$f"
        success=false
        break
    fi
done

if $success; then
    echo "檔名修改完成！"
fi
