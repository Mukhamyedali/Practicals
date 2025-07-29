STATE_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "SA": "South Australia",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

state = input("Enter short state: ").upper()
try:
    print(f"{state} is {STATE_NAMES[state]}")
except KeyError:
    print("Invalid short state")

for short, full in STATE_NAMES.items():
    print(f"{short:>3} is {full}")
