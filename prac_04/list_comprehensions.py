# list_comprehensions.py

numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

# List of numbers doubled
doubled = [number * 2 for number in numbers]
print("Doubled:", doubled)

# List of even numbers
evens = [number for number in numbers if number % 2 == 0]
print("Evens:", evens)

# List of strings from numbers
strings = [str(number) for number in numbers]
print("Strings:", strings)
