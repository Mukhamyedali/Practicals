from unreliable_car import UnreliableCar

my_bad_car = UnreliableCar("Old Bomb", 100, 50)

for i in range(10):
    distance = my_bad_car.drive(10)
    print(f"Attempt {i+1}: Drove {distance} km")
