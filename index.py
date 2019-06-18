# test_model.py

import numpy as np
from grabscreen import grab_screen
import cv2
import time
from directkeys import PressKey,ReleaseKey, W, A, S, D, Left, Right
from alexnet import alexnet
from getkeys import key_check

WIDTH = 80
HEIGHT = 63
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'minecraft-0.001-alexnetv2-8-epochs-4-data.model'

t_time = 0.09

def straight():
    PressKey(W)

def jump():
    PressKey(W)
    PressKey(Space)
    time.sleep(t_time)
    ReleaseKey(W)
    ReleaseKey(Space)

def left():
    PressKey(Left)
    time.sleep(t_time)
    ReleaseKey(Left)

def right():
    PressKey(Right)
    time.sleep(t_time)
    ReleaseKey(Right)

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):
        
        if not paused:
            # 800x600 windowed mode
            screen = grab_screen(region=(0,30,800,630))
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (80,63))

            prediction = model.predict([screen.reshape(80,63,1)])[0]

            moves = list(np.around(prediction))
            print(moves)

            fwd_thresh = 0.60
            mouse_thresh_maybe = 0.40

            if prediction[0] > fwd_thresh:
                straight()
            elif prediction[1] > mouse_thresh_maybe:
                left()
            elif prediction[2] > mouse_thresh_maybe:
                right()
            else:
                straight()

        keys = key_check()

        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(W)
                ReleaseKey(Right)
                ReleaseKey(Left)
                time.sleep(1)

main()       
