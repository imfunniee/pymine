import pyautogui, sys
try:
    while True:
        #moves your mouse ---> pyautogui.moveTo(100, 200)
        #gets direction
        x, y = pyautogui.position()
        positionStr = 'mouse-x: ' + str(x).rjust(4) + ' mouse-y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr),end='',flush=True)
except KeyboardInterrupt:
    print('\n')