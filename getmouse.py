import pyautogui, sys
from win32api import GetSystemMetrics

window_width =  GetSystemMetrics(0)
direction = 0
position = 0

try:
    while True:
        #gets direction
        x, y = pyautogui.position() #y could be used for looking up idk but for now meh
        if position == 0:
            direction = 0
            position = 0
            position = x
        else:
            if x != position:
                if x < window_width/2:
                    direction = 1
                    position = 0
                    position = x
                else:
                    direction = 2
                    position = 0
                    position = x
            else:
                direction = 0
                position = 0
        print(direction)
except KeyboardInterrupt:
    print('\n')

#0 = mouse doesn't move
#1 = move left
#2 = moved right

#pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)
