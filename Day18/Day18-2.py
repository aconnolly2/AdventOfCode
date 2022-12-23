import sys
sys.setrecursionlimit(20000)

def getAllNeighbors(c, rocks, neighbors, maxGrid):
    coordStr = f"{c[0]}-{c[1]}-{c[2]}"
    if coordStr in rocks or coordStr in neighbors or c[0] >= maxGrid[0] or c[1] >= maxGrid[1] or c[2] >= maxGrid[2] or c[0] <= -1 or c[1] <= -1 or c[2] <= -1:
        return neighbors
    else:
        neighbors[coordStr] = 1
        neighbors = getAllNeighbors([c[0]+1,c[1],c[2]], rocks, neighbors, maxGrid)
        neighbors = getAllNeighbors([c[0]-1,c[1],c[2]], rocks, neighbors, maxGrid)
        neighbors = getAllNeighbors([c[0],c[1]+1,c[2]], rocks, neighbors, maxGrid)
        neighbors = getAllNeighbors([c[0],c[1]-1,c[2]], rocks, neighbors, maxGrid)
        neighbors = getAllNeighbors([c[0],c[1],c[2]+1], rocks, neighbors, maxGrid)
        neighbors = getAllNeighbors([c[0],c[1],c[2]-1], rocks, neighbors, maxGrid)
        
    return neighbors

def checkAdjacencyContained(c, rocks, maxGrid):
    exposed = 6
    neighbors = {}
    if f"{c[0]+1}-{c[1]}-{c[2]}" in rocks:
        exposed -= 1
    else: # is cavern?
        neighbors.clear()
        neighbors = getAllNeighbors([c[0]+1,c[1],c[2]], rocks, neighbors, maxGrid)
        if "0-0-0" not in neighbors:
            exposed -= 1
            #print(f"cavern {c[0]+1},{c[1]},{c[2]}")
    if f"{c[0]-1}-{c[1]}-{c[2]}" in rocks:
        exposed -= 1
    else:     
        neighbors.clear()
        neighbors = getAllNeighbors([c[0]-1,c[1],c[2]], rocks, neighbors, maxGrid)
        if "0-0-0" not in neighbors:
            exposed -= 1        
            #print(f"cavern {c[0]-1},{c[1]},{c[2]}")
    if f"{c[0]}-{c[1]+1}-{c[2]}" in rocks:
        exposed -= 1
    else:
        neighbors.clear()
        neighbors = getAllNeighbors([c[0],c[1]+1,c[2]], rocks, neighbors, maxGrid)
        if "0-0-0" not in neighbors:
            exposed -= 1        
            #print(f"cavern {c[0]},{c[1]+1},{c[2]}")
    if f"{c[0]}-{c[1]-1}-{c[2]}" in rocks:
        exposed -= 1
    else:
        neighbors.clear()
        neighbors = getAllNeighbors([c[0],c[1]-1,c[2]], rocks, neighbors, maxGrid)
        if "0-0-0" not in neighbors:
            exposed -= 1                
            #print(f"cavern {c[0]},{c[1]-1},{c[2]}")
    if f"{c[0]}-{c[1]}-{c[2]+1}" in rocks:
        exposed -= 1
    else:
        neighbors.clear()
        neighbors = getAllNeighbors([c[0],c[1],c[2]+1], rocks, neighbors, maxGrid)
        if "0-0-0" not in neighbors:
            exposed -= 1              
            #print(f"cavern {c[0]},{c[1]},{c[2]+1}")
    if f"{c[0]}-{c[1]}-{c[2]-1}" in rocks:
        exposed -= 1
    else:
        neighbors.clear()
        neighbors = getAllNeighbors([c[0],c[1],c[2]-1], rocks, neighbors, maxGrid)
        if "0-0-0" not in neighbors:
            exposed -= 1                      
            #print(f"cavern {c[0]},{c[1]},{c[2]-1}")
    #print(neighbors)
    neighbors.clear()
    return exposed

coords = []
maxGrid=[]
occupiedPositions = {}

with open("./test18.txt") as inp:
    maxX = 0
    maxY = 0
    maxZ = 0
    for line in inp:
        c = line.strip().split(",")
        occupiedPositions[f"{c[0]}-{c[1]}-{c[2]}"] = 1
        coords.append([int(c[0]),int(c[1]),int(c[2])])
        maxX = max(int(c[0]), maxX)
        maxY = max(int(c[1]), maxY)
        maxZ = max(int(c[2]), maxZ)
        maxGrid = [maxX, maxY, maxZ]
        
print(maxGrid)
neighbors = {}
#neighbors = getAllNeighbors([0,2,5], occupiedPositions, neighbors, maxGrid)
#print("0-0-0" not in neighbors)


total = 0
for coord in coords:
    total += checkAdjacencyContained(coord, occupiedPositions, maxGrid)
    
print(total)