def f(i):
    if i%2 ==0:
        return True
    else:
        return False
    
import json
print(list(filter(f,[1,2,3,4])))
m = [-1,-2,-3,-4,-5]
for i,num in enumerate(m):
    print(i, num)

data = json.load(open(r'Final Lesson\info.json'))  

print(data)
for g in data:
    print(g)
    for a in data[g]:
        print(a, type(a))
json.dump({'test':[{1:2}]},open(r'Final Lesson\write.json','w'))