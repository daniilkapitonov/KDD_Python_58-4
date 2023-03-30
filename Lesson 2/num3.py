def filter_list(f,a,b,c):
    print(all(map(f,a)), list(map(f,a)))
    print(all(map(f,b)))
    print(all(map(f,c)))
    return [a if all(map(f,a)) else [],
            b if all(map(f,b)) else [],
            c if all(map(f,c)) else []]

a,b,c = [1,2,3,4],[23,-1],[None,[25]]
numbers = lambda a:type(a) in (int,float)
print(filter_list(numbers,a,b,c))

