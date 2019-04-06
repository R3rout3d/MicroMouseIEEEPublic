import csv

Pos = 0
i_j_current = [0, 0]

def movememnt(i_new, i_current, j_new, j_current): # resets current position and communicates movement
    if (i_new != i_current) and pos = 1:
        if (i_new < i_current):
            i_j_current[0] -= 1
            print(1)
        elif (i_new > i_current):
            i_j_current[0] += 1
            print(2)
    elif (j_new != j_current) and pos = 1:
        if (j_new < j_current):
            i_j_current[1] -= 1
            print(3)
        elif (j_new > j_current):
            i_j_current[1] +=1
            print(4)
     elif (i_new < i_current) and pos = 2:
            i_j_current[0] -= 1
            print(1)
        elif (i_new > i_current):
            i_j_current[0] += 1
            print(2)
    elif (j_new != j_current) and pos = 2:
        if (j_new < j_current):
            i_j_current[1] -= 1
            print(3)
        elif (j_new > j_current):
            i_j_current[1] +=1
            print(4)
    elif (i_new != i_current) and pos = 3:
        if (i_new < i_current):
            i_j_current[0] -= 1
            print(4)
        elif (i_new > i_current):
            i_j_current[0] += 1
            print(3)
    elif (j_new != j_current) and pos = 3:
        if (j_new < j_current):
            i_j_current[1] -= 1
            print(2)
        elif (j_new > j_current):
            i_j_current[1] +=1
            print(1)
     elif (i_new < i_current) and pos = 4:
            i_j_current[0] -= 1
            print(3)
        elif (i_new > i_current):
            i_j_current[0] += 1
            print(4)
    elif (j_new != j_current) and pos = 4:
        if (j_new < j_current):
            i_j_current[1] -= 1
            print(1)
        elif (j_new > j_current):
            i_j_current[1] +=1
            print(2)

ijstuff = []
nodeName = 'n'
nodeNumber = 0
nodeNode = ""

def csvWriter(node, i_j): # writes input to csv file
    with open("node.csv", "w") as f:
        fwrt = csv.writer(f, delimiter=',',
                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        fwrt.writerow([str(node), str(i_j[0]), str(i_j[1])])

def csvReader(rownum): # reads entirety of file and returns row
    with open("node.csv", "r") as f:
        csvr = csv.reader(f)
        csvr = list(csvr)
        return(csvr[int(rownum)])

def csvAppender(node, i_j):
    with open("node.csv", 'a') as f:
        fwrt = csv.writer(f, delimiter=',',
                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        fwrt.writerow([str(node), str(i_j[0]), str(i_j[1])])

def csvLength():
    with open("node.csv", "r") as f:
        csvl = csv.reader(f)
        for row in csvl:
            csvlr = []
            csvlr.append(csvl)
            print(len(csvlr))
            return(csvlr)

def csvReadAll():
    with open('node.csv', 'r') as f:
        for row in f:
            print(row)


#def csvLength(): # returns the length of the file
#    with open("node.csv", "r") as f:
#        csvr = csv.reader(f)
#        csvr = list(csvr)
#    return(len(csvr))

def AddNodes(i_j):
    ijstuff = []
    nodeName = 'n'
    nodeNumber = 0
    nodeNode = ""
    csvWriter('n0', ['0', '0'])
    for x in csvLength():
        if x == i_j:
            pass
        elif x != i_j:
            ijstuff.append(i_j[0])
            ijstuff.append(i_j[1])
            nodeNode = str(nodeName) + str(nodeNumber)
            csvAppender(nodeNode, ijstuff)
            nodeNumber += 1
