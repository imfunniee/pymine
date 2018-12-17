import pyautogui, sys
from win32api import GetSystemMetrics

def give_x():
    x, y = pyautogui.position() #y could be used for looking up idk but for now meh
    return x

last_mouse_movement = give_x()

def check_if_mouse_moved():
    now_mouse_movement = give_x()
    if now_mouse_movement != last_mouse_movement:
        return True
    else:
        return False 

def check_mouse():
    global last_mouse_movement
    direction = 0
    x_pos = give_x()
    if check_if_mouse_moved() == False:
        direction = 0
    else:
        #gets direction
        if x_pos < last_mouse_movement:
            direction = 1
            last_mouse_movement = give_x()
        else:
            direction = 2
            last_mouse_movement = give_x()
    print(last_mouse_movement)
    return direction

#0 = mouse doesn't move
#1 = move left
#2 = moved right
#pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)