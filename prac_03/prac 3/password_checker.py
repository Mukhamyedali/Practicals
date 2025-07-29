# password_checker.py

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print(f"\tand 1 or more special characters: {SPECIAL_CHARACTERS}")
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)} character password is valid: {password}")

def is_valid_password(password):
    if not MIN_LENGTH <= len(password) <= MAX_LENGTH:
        return False
    count_lower = sum(1 for c in password if c.islower())
    count_upper = sum(1 for c in password if c.isupper())
    count_digit = sum(1 for c in password if c.isdigit())
    count_special = sum(1 for c in password if c in SPECIAL_CHARACTERS)
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False
    if SPECIAL_CHARS_REQUIRED and count_special == 0:
        return False
    return True

main()
