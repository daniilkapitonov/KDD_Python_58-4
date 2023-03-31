m = [2,3,4,5,6,7,8,9]
for n in enumerate(m):
    print(n[0],n[1],n)
    m[n[0]] *=2
    if m[n[0]] % 2==0:
        m[n[0]]**=2

print(m)

m = [2,3,4,5,6,7,8,9]
for i,n in enumerate(m): #i = n[0] n=n[1] ^
    print(i,n)
    m[i] *=2
    if m[i] % 2==0:
        m[i]**=2

print(m)
