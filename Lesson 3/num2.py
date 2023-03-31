class Juice:
    def __init__(self,addition=None) -> None:
        self.addition = addition

    def my_juice(self):
        if self.addition == None:
            print("Сок без добавки")
        else:
            print("Сок с",self.addition)

j1 = Juice()
j2 = Juice("shugar")
print(j1.addition, j2.addition)
j1.addition = "water"
j1.my_juice()
j2.my_juice()