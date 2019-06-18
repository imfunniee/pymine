# balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load('training_data.npy')

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

forwards = []
mouse = []
nm = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1,0,0]:
        forwards.append([img,choice])
    elif choice == [0,0,1]:
        mouse.append([img,choice])
    elif choice == [0,1,0]:
        mouse.append([img,choice])
    elif choice == [0,0,0]:
        nm.append([img,choice])
    else:
        print('no matches')


forwards = forwards[:len(mouse)][:len(nm)]
mouse = mouse[:len(forwards)][:len(nm)]

final_data = forwards + nm + mouse
shuffle(final_data)

np.save('training_data_balanced.npy', final_data)
