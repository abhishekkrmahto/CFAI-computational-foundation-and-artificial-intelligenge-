path = ("left","right","up","down")
print(path)

path2 = [(0,0),(1,0),(2,0),(3,0),(4,0)]
for item in path2:
    print("visited",item)

dict = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
}

print(dict)

robo = {
    "x":0,
    "y":0
}

robo["x"] +=1
print(robo)


robo2 = {
    "name":"chitti robo",
    "steps":1000
}

print(robo2)

robo2.pop("steps") # removes the key val pair
print(robo2)