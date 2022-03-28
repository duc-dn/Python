import numpy as np 


# *Flatten is used to convert n-D into 1D
arr = np.arange(1, 11).reshape(5, 2)
print(arr)
print('arr after flattening: {}'.format(arr.flatten()))

