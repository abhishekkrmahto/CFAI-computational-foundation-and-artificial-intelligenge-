pos = [0,1]

print(pos[0],pos[1])


grid = [
    [1,2],
    [2,3]
]

print(grid[0][0])
print(grid[0][1])


moves = ["right","left","up","down"]

first_move = moves[:1]

print("first move = ",first_move)


path = []
path.append([0,0])
path.append([0,1])
print("Path = ",path)


moves = ["right","left","up","down"]
moves.insert(1,"left-east")
print(moves)


newMoves = ["left","right","up","down"]
newMoves.remove("left")
print(newMoves)
del newMoves[0]
print(newMoves)
newMoves.clear()
print(newMoves)