f = open('demo.txt', 'a')
f.write("Hello world")
f.close()

f = open('demo.txt', 'r')
print (f.read())