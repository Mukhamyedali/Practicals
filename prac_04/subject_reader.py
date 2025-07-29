# subject_reader.py

FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subjects(data)

def load_data():
    subjects = []
    with open(FILENAME) as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])  # Convert student number to int
            subjects.append(parts)
    return subjects

def display_subjects(subjects):
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]:3} students")

main()
