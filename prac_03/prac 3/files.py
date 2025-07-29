# files.py

# 1. Write name to file
name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

# 2. Read and greet
file = open("name.txt", "r")
name = file.read().strip()
file.close()
print(f"Hi {name}!")

# 3. Add first two numbers
with open("numbers.txt", "r") as file:
    first = int(file.readline())
    second = int(file.readline())
    print(first + second)

# 4. Add all numbers
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
print(total)
