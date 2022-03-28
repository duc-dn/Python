# Nếu try block sai thì khối except sẽ được biên dịch
print('\nEx1:')
try:
  print(x)
except:
  print("An exception occurred")

try:
  print(x)
except Exception as e:
  print(e)

# Bạn có thể sử dụng từ khóa else để xác định một khối mã sẽ 
# được thực thi nếu không có lỗi nào được phát sinh:
print('\nEx2:')
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


# Finally block sẽ được thực thi dù try block có lỗi hay là ko
print("\nEx3")
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


# Điều này có thể hữu ích để đóng các đối tượng và dọn dẹp tài nguyên:
print('\nEx4')
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")


x = 10
print('\nEx5:')
try:
  print(x)
except:
  print("An exception occurred")
else: 
  print('Sucessfull')