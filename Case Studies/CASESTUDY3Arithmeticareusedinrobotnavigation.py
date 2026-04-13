x = 0
y = 0

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
        y+=1
    elif(val == 2):
        y-=1
    elif(val == 3):
        x-=1
    elif(val == 4):
        x+=1
        
    else:
        break
    
    print("MOVED TO","[",x,y,"]")