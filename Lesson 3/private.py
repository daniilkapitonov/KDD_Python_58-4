import pandas


class Wheel:
    def __init__(self) -> None:
        self._radius = 18
        self.__x = 12

    def rad(self):
        print(self._radius)

class Car(Wheel):
    def __init__(self) -> None:
        self.name = "123"
        self.__q = 123
        self.__show()

    def __show(self):
        print("show")

c1 = Car()
# c1.__q = 123
# print(c1.__q)
# print(c1.__x)
c1.__show()

