import time
import threading
from pynput import keyboard
from mouse import MouseMovement

running = True


# 🔹 обработка нажатий клавиш (в отдельном потоке)
def on_press(key):
    global running
    running = False
    return False  # останавливает listener


def start_keyboard_listener():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    return listener


# 🔹 основной цикл движения мыши
def mouse_loop():
    global running

    mouse = MouseMovement()

    print("APP STARTED")

    while running:
        mouse.move_cursor()

        time.sleep(0.01)


if __name__ == "__main__":
    listener = start_keyboard_listener()

    try:
        mouse_loop()

    except KeyboardInterrupt:
        running = False

    print("APP FINNISHED")