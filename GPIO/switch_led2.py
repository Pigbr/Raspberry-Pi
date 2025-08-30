import curses
from gpiozero import LED

led = LED(18)

def main(stdscr):
    curses.cbreak()
    stdscr.nodelay(True)
    stdscr.keypad(True)

    stdscr.addstr(0, 0, "上下鍵控制 LED (↑=ON, ↓=OFF), q 離開")

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            led.on()
            stdscr.addstr(1, 0, "LED ON   ")
        elif key == curses.KEY_DOWN:
            led.off()
            stdscr.addstr(1, 0, "LED OFF  ")
        elif key == ord("q"):
            led.off()
            break

curses.wrapper(main)
