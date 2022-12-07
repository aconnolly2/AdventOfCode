from anytree import Node, RenderTree

def getChildByName(n, name):
    #print(n.children)
    for c in n.children:
        if (c.name == name):
            return c

inp = open("Input.txt")

tree_fs = Node('dir_/')
currentNode = tree_fs
for line in inp:
    if line.startswith("$ cd"):
        command = line.split(' ')
        targDir = command[2][:len(command[2]) - 1]
        if (targDir == ".."):
            currentNode = currentNode.parent
        else:
            targDir = 'dir_' + targDir
            currentNode = getChildByName(currentNode, targDir)
        #print(currentLocation)
    elif line.startswith("$ ls"):
        # Do nothing
        pass
    elif line.startswith("dir"):
        directory = line.split(' ')
        dirName = directory[1][:len(directory[1]) - 1]
        dirName = 'dir_' + dirName
        Node(dirName, parent = currentNode)
        #print(f"{dirName} added to {currentDir}")
    else:
        file = line.split(' ')
        fileName = file[1][:len(file[1]) - 1]
        Node(fileName, parent = currentNode, size = int(file[0]))
        #print(f"{fileName} of size {file[0]} added to {currentDir}")
    

inp.close()

# Part 1
def getDirectorySize(node):
    size = 0
    for c in node.children:
        if c.name.startswith('dir_'):
            size += getDirectorySize(c)
        else:
            size += c.size
    
    directorySizes[node] = size
    return size

directorySizes = {}
trueTotal = getDirectorySize(tree_fs)

total = 0
for key, value in directorySizes.items():
    if (value < 100000):
        total += value
    #print(f"{key} : {value}")
        
print(total)

# Part 2
sortedSizes = dict(sorted(directorySizes.items(), key=lambda item: item[1]))

target = 30000000 - (70000000 - trueTotal)
for key, value in sortedSizes.items():
    if value >= target:
        print(value)
        break