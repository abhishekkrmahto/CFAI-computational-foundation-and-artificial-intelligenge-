student = {
    "name":"Abhishek",
    "class":"10th",
    "subjects":["Physics","Chem","Maths"],
    "fees":900
}


print(student)
print(student["name"])


student["percentile"] = 86.41

print(student)

student["class"] = "12th"

for key,val in student.items():
    print(key,":",val)
    

