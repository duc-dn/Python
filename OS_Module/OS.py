import os

# Get current working directory
cwd = os.getcwd()
print(f"Working directory: {cwd}")

# Get all files in the root directory
list_files = os.listdir()
print(f"Listing files: {list_files}")

# Path
path = "/home"
 
# Join various path components
print(os.path.join(path, "User/Desktop", "file.txt"))

# Join various path components
path = "User/Documents"
print(os.path.join(path, "C:/", "file.txt"))

#* Ở ví dụ trên C:/ là một đường dẫn tuyệt đối nên tất cả các thành path bị bỏ qua

 