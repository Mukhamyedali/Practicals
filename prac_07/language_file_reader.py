from programming_language import ProgrammingLanguage

def main():
    languages = []
    with open("languages.csv", "r") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split(',')
            name, typing, reflection, year, pointer = parts
            language = ProgrammingLanguage(name, typing, reflection == "Yes", int(year), pointer == "Yes")
            languages.append(language)

    for language in languages:
        print(language)

if __name__ == '__main__':
    main()
