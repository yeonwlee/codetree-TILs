class People():
    def __init__(self, name: str = "", addr: str = "", city: str = ""):
        self.name = name
        self.addr = addr
        self.city = city

    def print_data(self):
        print(f"name {self.name}")
        print(f"addr {self.addr}")
        print(f"city {city}")

    
num_of_people = int(input())
people = []

for _ in range(num_of_people):
    name, addr, city = input().split()
    people.append(People(name, addr, city))

people.sort(key=lambda person: person.name, reverse=True)
people[0].print_data()