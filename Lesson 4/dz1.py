import time

def print_all(*a, sep = " ", end = "\n"):
    return (sep.join([str(i) for i in a]))+end

def print_all1(*a, sep = " ", end = "\n"):
    return (sep.join(map(str,a)))+end

start = time.time()
for i in range(300):
    print(print_all(1,2,3,4,5,2,3,4,52,3,4,52,3,4,52,3,4,52,3,4,5, sep="a", end='!'))

end1 = time.time()-start

start = time.time()
for i in range(300):
    print(print_all1(1,2,3,4,5,2,3,4,52,3,4,52,3,4,52,3,4,52,3,4,5, sep="a", end='!'))

end2 = time.time()-start

print('end1', end1, 'end2', end2)