"""
Emails
Estimate: 15 minutes
Actual: 14 minutes
"""

def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmed = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmed != "y" and confirmed != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    return " ".join(part.capitalize() for part in parts)

main()
