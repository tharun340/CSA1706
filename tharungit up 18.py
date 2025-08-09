people_db = [
    {"name": "John Doe", "dob": (1990, 5, 15)},
    {"name": "Jane Smith", "dob": (1985, 12, 3)},
    {"name": "Alice Walker", "dob": (2000, 1, 23)},
    {"name": "Bob Johnson", "dob": (1995, 7, 30)},
    {"name": "Susan Clark", "dob": (1978, 9, 12)}
]


def list_people():
    print("All people in the database:")
    for person in people_db:
        name = person["name"]
        dob = person["dob"]
        print(f"Name: {name}, DOB: {dob[0]:04d}-{dob[1]:02d}-{dob[2]:02d}")

def find_by_name(name):
    for person in people_db:
        if person["name"].lower() == name.lower():
            y, m, d = person["dob"]
            print(f"{name}'s DOB is: {y:04d}-{m:02d}-{d:02d}")
            return
    print(f"No entry found for name: {name}")

def born_in_year(year):
    found = False
    print(f"People born in {year}:")
    for person in people_db:
        if person["dob"][0] == year:
            name = person["name"]
            y, m, d = person["dob"]
            print(f"{name} - {y:04d}-{m:02d}-{d:02d}")
            found = True
    if not found:
        print("No one found born in that year.")

def add_person(name, year, month, day):
    people_db.append({"name": name, "dob": (year, month, day)})
    print(f"Added {name} to the database.")



if __name__ == "__main__":
    list_people()
    print("\n---\n")
    find_by_name("Alice Walker")
    print("\n---\n")
    born_in_year(1990)
    print("\n---\n")
    add_person("Tom Hardy", 1988, 11, 20)
    print("\n---\n")
    list_people()
