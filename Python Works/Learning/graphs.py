graph = {
    "A":['C','B'],
    "B":['A','D'],
    "C":['A','D'],
    "D":['B','C'],
    "E":[],
    "F":[]
}

print(graph)

print(len(graph))

print("NEIGBOUR OF A = ",graph["A"])
print("NEIGBOUR OF B = ",graph["B"])

for node in graph:
    print(node,"=",graph[node])

for node in graph:
    print(node,"connected to",graph[node])


places  = ['1','2','3','4','5','6','7','8','9']

graph = [places]

ans = ""

for node in graph[0]:
    ans = ans + node+" "

print(ans)


grid =[
    [0,1],
    [0,0],
    [1,0],
    [1,1],
]


graph ={
    "A":{"B":5,"C":2,"D":4,"E":3,"F":6}
}

min_cost = min(graph["A"].values())
max_cost = max(graph["A"].values())

cheapestNode = graph["A"].get(min_cost)

print("MIN = ",min_cost," NODE = ",cheapestNode)
print("MAX = ",max_cost)