#!/bin/bash
# 分類檔案到不同資料夾

target_dir="$(pwd)"
mkdir -p "$target_dir/Images" "$target_dir/Documents" "$target_dir/Archives"

for file in "$target_dir"/*; do
    if [[ $file == *.jpg || $file == *.png ]]; then
        mv "$file" "$target_dir/Images/"
    elif [[ $file == *.pdf || $file == *.txt ]]; then
        mv "$file" "$target_dir/Documents/"
    elif [[ $file == *.zip || $file == *.tar.gz ]]; then
        mv "$file" "$target_dir/Archives/"
    fi
done

echo "整理完成！"
