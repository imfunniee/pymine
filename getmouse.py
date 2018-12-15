import pyautogui, sys
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'mouse-x: ' + str(x).rjust(4) + ' mouse-y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr),end='',flush=True)
except KeyboardInterrupt:
    print('\n')