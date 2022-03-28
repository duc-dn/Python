import numpy as np 

arr = np.arange(1, 10).reshape(3,-1)
print('Sum of arr follow rows = {}'.format(arr.sum(axis=1)))
print('Sum of arr follow columns = {}'.format(arr.sum(axis=0)))


new_arr = np.arange(1,10).reshape(3,-1)
print(new_arr)
print('Arr after flattening = {}'.format(new_arr.flatten()))