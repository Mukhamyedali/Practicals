from car import Car

def main():
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Fuel in limo: {limo.fuel}")
    distance_driven = limo.drive(115)
    print(f"Distance driven: {distance_driven}")
    print(limo)

main()
