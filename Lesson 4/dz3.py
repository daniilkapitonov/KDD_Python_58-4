class Student:
    def_name = "Ivan"
    def_age = 18
    def_group_number = "10A"
    def __init__(self, name = def_name,group_number = def_group_number, age = def_age) -> None:
        if name == Student.def_name or age == Student.def_age:
            self.__def_check_age_name = True
        else:
            self.__def_check_age_name = False

        if group_number == Student.def_group_number:
            self.__def_check_gr = True
        else:
            self.__def_check_gr = False
        self.name = name
        self.group_number = group_number
        self.age = age

    def getname(self):
        print(self.name)
    def getage(self):
        print(self.age)
    def getgroup_number(self):
        print(self.group_number)

    def setNameAge(self, name, age):
        if self.__def_check_age_name:
            self.age = age
            self.name = name
            self.__def_check_age_name = False
        else:
            print("Change is not possible NA")

    def setGroupNumber(self, gr):
        if self.__def_check_gr:
            self.group_number = gr
            self.__def_check_gr = False
        else:
            print("Change is not possible GR")

s1 = Student()
s2 = Student(group_number="ABC")
s3 = Student("Peta","43M",23)
s1.getname()
s1.setNameAge("Sonua",20)
s1.setGroupNumber("21A")
print()
s2.setNameAge("Sonua",20)
s2.setGroupNumber("21A")
print()
s3.setNameAge("Sonua",20)
s3.setGroupNumber("21A")
print()
s1.getname()