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
     if (i_new < i_current):
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
     if (i_new < i_current):
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

    


def csvWriter(node, i_j): # writes input to csv file
    with open("node.csv", "w") as f:
        fwrt = csv.writer(csvfile, delimiter=',',
                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        fwrt.writerow([str(node), str(i_j[0], str(i_j[1])])

def csvReader(rownum): # reads entirety of file and returns row
    with open("node.csv", "r") as f:
        csvr = csv.reader(f)
        csvr = list(csvr)
     return(csvr[int(rownum)])

def csvLength(): # returns the length of the file
    with open("node.csv", "r") as f:
        csvr = csv.reader(f)
        csvr = list(csvr)
    return(len(csvr))
        
def node(): # writes the node to the file
    node_name = csvLength()
    node_i_j = i_j_current[]
    csvWriter(node_name, node_i_j)
