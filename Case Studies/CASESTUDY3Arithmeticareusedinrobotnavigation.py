left = 0
right = 0
up = 0
down = 0

while(True):
    print("ENTER 0 FOR EXIT:- ")
    print("ENTER 1 FOR UP:- ")
    print("ENTER 2 FOR DOWN:- ")
    print("ENTER 3 FOR LEFT:- ")
    print("ENTER 4 FOR DOWN:- ")

    val = int(input())
    if(val == 0):
        break
    
    if(val == 1):
        up+=1
    elif(val == 2):
        down+=1
    elif(val == 3):
        left+=1
    elif(val == 4):
        right+=1 