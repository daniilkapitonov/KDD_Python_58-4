class Person:
    def __init__(self,name,age,number,address):
        self.name = name
        self.age = age
        self.number = number
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}, age: {self.age}\nNumber: {self.number}, Address: {self.address}"

class Book:
    def __init__(self, p:Person = None) -> None:
        self.people = dict()
        if p != None:
            self.add(p)

    def add(self, p:Person):
        if p.name not in self.people.keys():
            self.people[p.name] = []
        self.people[p.name].append(p)

    def add_list(self, per_list):
        for p in per_list:
            self.add(p)

    def __str__(self):
        s = "Список людей:\n"
        for people_l in self.people.values():
            for people in people_l:
                s+= str(people) + '\n'
        return s
    
    def remove(self, name,age):
        for item in self.people.items():
            for people in item[1]:
                if people.name == name and people.age == age:
                    cash = item
                    cash[1].remove(people)
                    self.people[item[0]] = cash[1]
                    return True
        return False

    def find_by_street(self,s):
        for people_l in self.people.values():
            for people in people_l:
                if people.address == s:
                    return people
        return False

p1 = Person('Polina', 21, 4, "Vavilova 32")
p2 = Person('Efim', 21, 4, "Vavilova 32")
p3 = Person('Polina', 23, 6, "Novay 32")
print(p1)
l = [p1,p2,p3]
b = Book(p1)
b.add_list(l)
print(b.people)
print(b.find_by_street('Vavilova 32'))
print(b)
print(b.remove('Polina',23))
print(b)