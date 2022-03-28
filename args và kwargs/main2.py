# *Varriable-length parameter (*args and **kwargs)

# *If you mark a parameter with one asterisk (*)
# *You can pass any number of positional arguments to your function (Typicall called *args)
# *If you mark a parameter with two asterisk (**)
# *you can pass any number of keyword arguments to this function (Typicall called **kwargs)


# *args like list (arg: arguments)
# *kwargs (kwargs: keyword arguments) like Dict
# (args, kwargs can rename any name that you want 

def variableLengthArgExample(a,b, *args, **kwargs):
    print(a, b) 
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

def main():
    # variableLengthArgExample('a', 'b', 'Hellow World', 1, 2, 3)
    # **kwargs
    variableLengthArgExample('a', 2, "Hello World", 1, size="Up Size", age = "18")

if __name__ == "__main__":
    main()