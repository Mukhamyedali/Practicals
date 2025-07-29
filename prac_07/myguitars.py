from guitar import Guitar

FILENAME = "guitars.csv"

def load_guitars():
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def save_guitars(guitars):
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

def display_guitars(guitars):
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

def main():
    guitars = load_guitars()
    guitars.sort()
    print("These are my guitars:")
    display_guitars(guitars)

    print("\nAdd new guitars:")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))

    guitars.sort()
    save_guitars(guitars)

if __name__ == '__main__':
    main()
