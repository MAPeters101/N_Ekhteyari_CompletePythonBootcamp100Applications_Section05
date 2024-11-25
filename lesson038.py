
with open('lesson021.py', 'r') as file:
    content = file.readlines()
    i = 1
    for line in content:
        print(f"Line {i}: {line}", end='')
        i += 1

print()

with open('file2.txt', 'r') as file:
    content = file.readlines()
    i = 1
    for line in content:
        print(f"Line {i}: {line.strip()}")
        i += 1

print()




