class Ball:
    def __init__(self,size, typ, color):
        self.size = size
        self.typ = typ
        self.color = color
        self.weight = size*30
    
    def set_color(self,color):
        self.color = color

    def set_size(self,size):
        self.size = size
        self.weight = self.size *30

b1 = Ball(32,'football','white')
print(b1.color,b1.size,b1.typ, b1.weight)
b1.set_color('red')
b1.set_size(65)
print(b1.color,b1.size,b1.typ, b1.weight)

        