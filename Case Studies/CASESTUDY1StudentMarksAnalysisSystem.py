stdName = input("Enter Student Name- ")

marks = []

no_of_subjects = int(input("Enter Number of subjects:- "))

total = 0

for i in range(no_of_subjects):
    marks.append(int(input("ENTER MARK:- ")))
    total+=marks[i]
    
percentage = total/no_of_subjects

print("YOUR PERCENTAGE:- ",percentage)