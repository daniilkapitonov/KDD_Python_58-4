class Wheel:
    def __init__(self) -> None:
        self._radius = 18
        self.__x = 12

    def rad(self):
        print(self._radius)

class Car(Wheel):
    car_count = 0
    obj_list = []


    def __init__(self):
        super().__init__()
        self.name = "Lada"
        self._color = "Red"
        Car.car_count +=1
        Car.obj_list.append(self)
        self.b = "asdasd"
        # self.__x = 123
        
    def rad(self):
        print('asdasdasdasd')
        return super().rad()

    def s1(self):
        print('s1')

    @classmethod
    def start(cls):
        print(Car.obj_list)
        print('Class', cls.__name__)

    @staticmethod
    def s2():
        
        print('s2')
    # del __(self):



c1 = Car()
c1._color = "asd"
c1._radius = 123123
c2 = Car()
c3 = Car()
c4 = Car()
c5 = Car()
c5.__x = 123
print(c5.__x,'c5 X')
del c5
c2.rad()
print(c1.car_count,c2.car_count,c3.car_count)

Car.start()
Car.obj_list[0].name = 'Chery'
print(Car.obj_list[0].name,c1.name)

# c1.start()
# Car.s1()
# Car.s2()