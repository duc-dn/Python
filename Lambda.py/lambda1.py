coordinate2D = [(6,9), (-1,3), (2,10)]

# sorting follow x
print(sorted(coordinate2D))

# sorting follow y
print(sorted(coordinate2D, key=lambda point: point[1]))


# =============================
number_list = [5,3,-2,4,1,-1,-3,4,5]
print(sorted(number_list))
print(sorted(number_list, key=lambda x: abs(x)))

#==================================
# Dung lambda trong map function
# Map transforms each element with the function 
# map(func, list)
list_keyword = ["codexplore", "welcome", "cac ban"]

print(list(map(lambda x:x.title(), list_keyword)))

# mot cach khac dung List comprehension
new_list = [i.title() for i in list_keyword]
print(new_list)

# Use with filter 
list_number = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2==1, list_number)))
new_nums = [i for i in list_number if i%2==1]
print(new_nums)


# Use lambda for reduce function 
