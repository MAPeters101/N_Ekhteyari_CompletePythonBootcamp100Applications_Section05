
# with open("file039.txt", 'a') as file:
#     file.write("\nAppending new content to the file.")
#
# with open("files039.txt", 'r') as file:
#     file.write("\nAppending new content to the file.")
#

file_path = "file/file039.txt"
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File not found: {file_path}")



