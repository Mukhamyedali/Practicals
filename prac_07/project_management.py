from project import Project
from datetime import datetime

FILENAME = "projects.txt"

def load_projects(filename):
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split('\t')
            name, start, priority, cost, complete = parts
            projects.append(Project(name, start, int(priority), float(cost), int(complete)))
    return projects

def save_projects(filename, projects):
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)

def display_projects(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]
    print("Incomplete projects:")
    for p in sorted(incomplete):
        print(f"  {p}")
    print("Completed projects:")
    for p in sorted(complete):
        print(f"  {p}")

def filter_projects(projects, filter_date):
    print(f"Projects after {filter_date}:")
    for p in sorted(projects, key=lambda p: datetime.strptime(p.start_date, "%d/%m/%Y")):
        if datetime.strptime(p.start_date, "%d/%m/%Y") > filter_date:
            print(p)

def add_project():
    name = input("Name: ")
    start = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    complete = int(input("Percent complete: "))
    return Project(name, start, priority, cost, complete)

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_completion:
        project.completion_percentage = int(new_completion)
    if new_priority:
        project.priority = int(new_priority)

def main():
    projects = load_projects(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    MENU = """- (L)oad projects  - (S)ave projects  - (D)isplay projects  - (F)ilter projects by date
- (A)dd new project  - (U)pdate project  - (Q)uit"""
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_date = datetime.strptime(date_string, "%d/%m/%Y")
            filter_projects(projects, filter_date)
        elif choice == 'a':
            project = add_project()
            projects.append(project)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").lower()
    print("Would you like to save to projects.txt?")
    response = input(">>> ").lower()
    if response in ('yes', 'y'):
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")

if __name__ == '__main__':
    main()
