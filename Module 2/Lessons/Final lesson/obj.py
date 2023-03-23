from random import randint
class Ball:
    def __init__(self, color="def", weight = 0, typ = "def"):
        print("Hello! You've create your class!")
        self.color = color
        self.typ = typ #футбол, баскет, волейбол и т.д.
        self.weight = weight
    def show_info(self):
        print("Мяч, цвета -",self.color,"он нужен для игры в -", self.typ,"его вес -", self.weight)
    def edit_color(self,c):
        self.color = c

class Wardrobe(Ball):
    def __init__(self):#, color="def", weight=0, typ="def"):
        self.mass_ball = []
        col = ["red", "green","blue","white"]
        for i in range(9):
            self.mass_ball.append(Ball(col[randint(0,len(col)-1)],randint(0,10), "Football"))
            self.mass_ball[i].show_info()
        super().__init__()


w1 = Wardrobe()
w1.color = "Purple"
w1.show_info()


b1 = Ball("red",3.2,"Basketball")
# b1.color = "Red"
# b1.typ = "Footbal"
# b1.weight = 1.2
b1.show_info()
# b1.edit_color("Blue")
# b1.show_info()
print(b1.color, b1.typ, b1.weight)

b2 = Ball()
b2.show_info() 
print(b2.color, b2.typ, b2.weight)

mass = []
mass.append(b1)
mass.append(b2)
print(mass[0].color)
# qwe = "qwe"
# print(type(b1))
# print(type(qwe))

