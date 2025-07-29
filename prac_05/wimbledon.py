"""
Wimbledon
Estimate: 25 minutes
Actual: 22 minutes
"""

FILENAME = "wimbledon.csv"

def main():
    records = load_data()
    champions_to_wins, countries = process_data(records)
    display_results(champions_to_wins, countries)

def load_data():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        return [line.strip().split(",") for line in in_file.readlines()[1:]]

def process_data(records):
    champions_to_wins = {}
    countries = set()
    for year, winner, country in records:
        champions_to_wins[winner] = champions_to_wins.get(winner, 0) + 1
        countries.add(country)
    return champions_to_wins, countries

def display_results(champions_to_wins, countries):
    print("Wimbledon Champions:")
    for champ, wins in champions_to_wins.items():
        print(f"{champ} {wins}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

main()
