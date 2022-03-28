mylist = ["apple", "banana", "cherry"]
print (mylist)


# acess list items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#Check if "apple" is present in the list:
thislist2 = ["apple", "banana", "cherry"]
if "apple" in thislist2:
    print("Yes, 'apple' is in the fruits list")


# add item in list 
thislist3 = ["apple", "banana", "cherry"]
thislist3.append("orange")
print(thislist3)

# Loop through list 
for x in thislist3:
    print(x)

print('\nShow list')
for i in range(len(thislist3)):
    print (thislist3[i])

# short hand for loop 
#A short hand for loop that will print all items in a list:
print ("\nShort hand: ") 
[print (x) for x in thislist3]