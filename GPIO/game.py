import curses
import random
import time

def main(stdscr):
    # 隱藏游標
    curses.curs_set(0)

    # 檢查終端機大小
    sh, sw = stdscr.getmaxyx()
    if sh < 20 or sw < 40:
        stdscr.addstr(0, 0, "請把終端機調大到至少 20x40 再玩")
        stdscr.refresh()
        stdscr.getch()
        return

    # 建立新視窗
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    # 顏色設定
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # 蛇
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # 食物
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)   # 邊界
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK) # 分數

    # 畫邊界
    for x in range(sw-1):
        w.addch(0, x, '#', curses.color_pair(3))
        w.addch(sh-2, x, '#', curses.color_pair(3))
    for y in range(sh-1):
        w.addch(y, 0, '#', curses.color_pair(3))
        w.addch(y, sw-2, '#', curses.color_pair(3))

    # 初始化蛇與食物
    snk_x = sw//4
    snk_y = sh//2
    snake = [[snk_y, snk_x],
             [snk_y, snk_x-1],
             [snk_y, snk_x-2]]
    food = [random.randint(1, sh-3), random.randint(1, sw-3)]
    w.addch(food[0], food[1], '●', curses.color_pair(2))

    key = curses.KEY_RIGHT
    score = 0
    w.addstr(0, 2, f'Score: {score}', curses.color_pair(4))

    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        # 計算蛇頭新座標
        head = snake[0][:]
        if key == curses.KEY_DOWN: head[0] += 1
        elif key == curses.KEY_UP: head[0] -= 1
        elif key == curses.KEY_LEFT: head[1] -= 1
        elif key == curses.KEY_RIGHT: head[1] += 1

        # 撞牆或撞自己
        if head[0] in [0, sh-2] or head[1] in [0, sw-2] or head in snake:
            w.addstr(sh//2, sw//2-5, "GAME OVER", curses.color_pair(2))
            w.refresh()
            time.sleep(2)
            break

        snake.insert(0, head)

        # 吃食物
        if head == food:
            score += 1
            w.addstr(0, 2, f'Score: {score} ', curses.color_pair(4))
            food = None
            while food is None:
                nf = [random.randint(1, sh-3), random.randint(1, sw-3)]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], '●', curses.color_pair(2))
            # 提升速度
            w.timeout(max(50, 100 - (score*2)))
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        # 畫蛇頭
        w.addch(snake[0][0], snake[0][1], '■', curses.color_pair(1))

curses.wrapper(main)