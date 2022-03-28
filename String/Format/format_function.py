import numpy as np 

if __name__ == "__main__":
    arr = np.arange(1, 10).reshape(3,-1)
    print('Sum of arr follow rows = {}'.format(arr.sum(axis=1)))
    print('Sum of arr follow columns = {}'.format(arr.sum(axis=0)))