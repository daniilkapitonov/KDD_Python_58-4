floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 
          34.23, 12.12, 4.67, 2.45, 9.32]

def round_square(x):
    return round(x**2,1)

print(list(map(round_square,floats)))