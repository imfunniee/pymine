# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi
import win32con
import time

keyList = ["\b"]
left = win32con.VK_LEFT
right = win32con.VK_RIGHT

for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    if wapi.GetAsyncKeyState(left):
            keys.append('LEFT')
    if wapi.GetAsyncKeyState(right):
            keys.append('RIGHT')
    return keys