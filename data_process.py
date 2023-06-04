import pandas as pd
import numpy as np
import random

def load_data(path_old, path_new):
    fer2013 = pd.read_csv(path_old)
    fer_new = pd.read_csv(path_new)
    label = np.array(fer_new)[:,2:]
    print(fer2013)
    print(label)

    for i in range(len(label)):
        max_indices = np.argwhere(label[i] == np.amax(label[i]))
        selected_emotion = random.choice(max_indices)
        fer2013['emotion'][i] = int(selected_emotion)
        
    print(fer2013)

    fer2013.to_csv('./fer2013_new.csv', index=False)

if __name__ == '__main__':
    path_old = 'data/fer2013.csv'
    path_new = 'data/fer2013new.csv'
    load_data(path_old, path_new)
