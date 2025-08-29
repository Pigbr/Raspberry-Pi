#!/bin/bash

# 列出所有非 .sh 的檔案
files_to_delete=()
for f in *; do
    if [[ ! $f == *.sh ]]; then
        files_to_delete+=("$f")
    fi
done

# 顯示要刪除的檔案
echo "以下檔案將被刪除："
printf "%s\n" "${files_to_delete[@]}"

# 確認後再刪除
read -p "確定要刪除嗎？(y/N) " confirm
if [[ $confirm == [yY] ]]; then
    rm -rf "${files_to_delete[@]}"
    echo "已刪除！"
else
    echo "已取消刪除。"
fi
