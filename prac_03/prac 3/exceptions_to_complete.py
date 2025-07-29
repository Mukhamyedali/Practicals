# exceptions_to_complete.py

finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a valid integer: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print(f"Valid result is: {result}")
