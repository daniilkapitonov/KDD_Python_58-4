import random
def gen_mass(n):
    cash = []
    for i in range(n):
        cash.append(random.randint(0,10))
    return cash

print(gen_mass(34))
