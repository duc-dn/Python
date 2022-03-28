#* The map() function executes a specified function for each item in an iterable.
#  The item is sent to the function as a parameter

def my_func(a):
    return len(a)

x = map(my_func, ('banana', 'longan', 'dragonfruit', 'mango'))
print(list(x))


# EX2
def my_func2(a, b):
    return a + b

y = map(my_func2, [1, 2, 3, 4], [5, 6,7, 8])
print(list(y))