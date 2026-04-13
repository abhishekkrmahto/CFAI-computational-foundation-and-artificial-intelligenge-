s = {101,102,103,104,101}

for i in s:
    print(str(i))



print(101 in s)
print(101 not in s)

s.add(106)
print(s)

setA = {101,110,102,103}
setB = {101,108,105}

newSet = setA.union(setB)
print(newSet)

newSetINter = setA.intersection(setB)
print(newSetINter)

set1 ={1,2,3}
set2 = {'a','b','c'}
set1.update(set2)
print(set1)