from silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 4)
hummer.drive(18)
print(hummer)
print(f"Fare: ${hummer.get_fare():.2f}")
