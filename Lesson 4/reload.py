class Apple_tree:
    def __init__(self,name = 'lower', vetka_count = 1, apple_on_v = 1):
        self.name = name
        self.vetka_count = vetka_count
        self.apple_on_v = apple_on_v
    
    def __add__(self,second): #складываем кол-во яблок на ветке
        cash = Apple_tree()
        cash.apple_on_v = self.apple_on_v + second.apple_on_v
        return cash
    
    def __mul__(self,second):
        cash = Apple_tree()
        cash.vetka_count = self.vetka_count + second.vetka_count
        return cash
    
    def __str__(self):
        return f"Name {self.name}, vetok - {self.vetka_count}, apples - {self.apple_on_v}"

v1 = Apple_tree()
v2 = Apple_tree()
v3 = v1+v2
print(v1.apple_on_v)
print(v3.apple_on_v)
v1+=v2
print(v1.apple_on_v)

print((v1*v2*v1*v2).vetka_count)
v1*=v2
print(v1)

