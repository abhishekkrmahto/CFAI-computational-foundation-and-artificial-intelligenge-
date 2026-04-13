list = ["red","green","blue"]


print(list)

print("COLOUR AT 1 = "+str(list[0]))
print("COLOUR AT 2 = "+str(list[1]))
print("COLOUR AT 3 = "+str(list[2]))

# or we can give -1 -2 .... from last for index


list.append("pink")


print("After appending pink = "+str(list))


listb = ["hii","hello"]

list.append(listb)

print("AFTER APPENDING LISTB = "+str(list))


listb.clear()


print("LIST B is clearer !!"+str(listb))


copyLisy = list.copy()


print("LIST IS COPIED TO COPYLIST = " + str(copyLisy))

list.append("red")

length = list.count("red")


print("RED IN LIST = "+str(length)+" Times")


print("INDEX OF blue = "+str(list.index("blue")))

x= list.index("red",1)

print("SECOND TIME APPPEARING RED INDEX  = "+str(x))

list.remove("red")

print("After removing red = "+str(list))

list.reverse()

print("AFTER rev == "+str(list))

nums = [1,2,34,1,6,22]
nums.sort()

print("AFTER SORTING = "+str(nums))

nums.sort(reverse=True)

print("AFTER SORTING and reverse = true = "+str(nums))


print("[1:3] = "+str(list[1:3]))
print("[:3] = "+str(list[:3]))
print("[1:] = "+str(list[1:]))


list[1] = "abhishek"

print("ADDED AR INDEX 1 = "+str(list))

nums[1:3] = [20,30,40,60]

print("nums[1:2] = [20,30] = "+str(nums))





