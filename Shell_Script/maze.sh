#!/bin/bash

# 顏色設定
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # 無色

# 迷宮地圖 (#=牆壁, 空格=路, S=起點, E=終點)
map=(
"###############"
"#S    #      E#"
"# ### # #######"
"#     #       #"
"### ####### # #"
"#             #"
"###############"
)

# 玩家初始位置
player_x=1
player_y=1
steps=0

# 畫出迷宮
draw_map() {
    clear
    for y in "${!map[@]}"; do
        line="${map[$y]}"
        if [[ $y -eq $player_y ]]; then
            line="${line:0:$player_x}${GREEN}P${NC}${line:$((player_x+1))}"
        fi
        echo -e "$line"
    done
    echo "步數: $steps"
}

# 移動玩家
move_player() {
    local nx=$player_x
    local ny=$player_y
    case $1 in
        w) ((ny--)) ;;
        s) ((ny++)) ;;
        a) ((nx--)) ;;
        d) ((nx++)) ;;
    esac

    # 檢查牆壁
    if [[ "${map[$ny]:$nx:1}" != "#" ]]; then
        player_x=$nx
        player_y=$ny
        ((steps++))
    fi
}

# 遊戲主迴圈
while true; do
    draw_map
    if [[ "${map[$player_y]:$player_x:1}" == "E" ]]; then
        echo -e "${RED}恭喜你到達終點！總步數: $steps${NC}"
        break
    fi
    echo "使用 w/a/s/d 移動"
    read -n1 move
    move_player "$move"
done

