import pyautogui, sys
from win32api import GetSystemMetrics

def give_x():
    x, y = pyautogui.position() #y could be used for looking up idk but for now meh
    return x

last_mouse_movement = give_x()

def check_if_mouse_moved():
    now_mouse_movement = give_x()
    if now_mouse_movement != last_mouse_movement:
        last_mouse_movement = give_x()
        return True
    else:
        return False 

def check_mouse():
    direction = 0
    x_pos = give_x()
    if check_if_mouse_moved() == False:
        direction = 0
    else:
        window_width =  GetSystemMetrics(0)
        #gets direction
        if x_pos < window_width/2:
            direction = 1
        else:
            direction = 2
    return check_if_mouse_moved()

#0 = mouse doesn't move
#1 = move left
#2 = moved right
#pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)