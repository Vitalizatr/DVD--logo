import time

from pynput import keyboard

from mouse import MouseMovement,mouse

running = True

def on_press_any_key(key):
    global running
    running = False

listener = keyboard.Listener(on_press=on_press_any_key)
listener.start()
   
"""
mouse = MouseMovement() 

    while running:
        mouse.move_cursor()
        time.sleep(1/120) 
"""
if __name__ == "__main__":

    print(mouse.position)