# Eric Xie hx8rc
import math
import heapq
import copy


class Point:
    def __init__(self, x, y, cat):
        self.x = x
        self.y = y
        self.dist = 0
        self.cat = cat
    def distance(self, p):
        temp = pow((self.x-p.x),2)+pow((self.y-p.y),2)
        return math.sqrt(temp)

    def __lt__(self, other):
        return self.dist < other.dist


def processdata(filename, m):
    data = []
    count = 0
    with open(filename, 'r') as datafile:
        for line in datafile:
            if count == m:
                return data
            entry = line.split()
            cat = entry[0]
            d_x = float(entry[1])
            d_y = float(entry[2])
            dataPoint = Point(d_x, d_y, cat)
            data.append(dataPoint)
            count=count+1
    if count<m:
        print("Note: Number of data points in the file was less than M")
    return data


def categorize(pt, dataset, k):
    localData = copy.deepcopy(dataset)
    for i in range(len(localData)):
        localData[i].dist = localData[i].distance(pt)
    heapq.heapify(localData)
    cat1 = ["",0,0]
    cat2 = ["",0,0]
    for i in range(k):
        temp = heapq.heappop(localData)
        print("{0} {1} {2} {3}".format(temp.cat,temp.x,temp.y,temp.dist))
        if temp.cat==cat1[0]:
            cat1[2]+=1
            cat1[1]+=temp.dist
        elif temp.cat==cat2[0]:
            cat2[2]+=1
            cat2[1]+=temp.dist
        elif cat1[0]=="":
            cat1[0]=temp.cat
            cat1[1]+=temp.dist
            cat1[2]+=1
        elif cat2[0] == "":
            cat2[0]=temp.cat
            cat2[1]+=temp.dist
            cat2[2]+=1
    if cat1[2]>cat2[2]:
        pt.cat=cat1[0]
    else:
        pt.cat=cat2[0]
    print("The data pair [", pt.x, ",", pt.y, "] is assigned to category: ", pt.cat, sep='')
    avg1 = 0
    avg2 = 0
    if cat1[2]!=0:
        avg1 = cat1[1] / cat1[2]
    if cat2[2]!=0:
        avg2 = cat2[1] / cat2[2]
    print("Average distance to",cat1[0],"items: ","{0:.3f}".format(avg1))
    print("Average distance to",cat2[0],"items: ","{0:.3f}".format(avg2))
while True:
    try:
        k = int(input("Please enter the value of k: "))
        break
    except ValueError:
        print("k must be an integer. Try again...")
while True:
    try:
        m = int(input("Please enter the value of M: "))
        break
    except ValueError:
        print("M must be an integer. Try again...")
if k>m:
    print("k > M, setting k = M...")
    k=m
filename = input("Specify the name of the data file: ")
data = processdata(filename, m)
while True:
    newPair = input("Enter a data pair (Enter \"1.0 1.0\" to quit): ")
    while len(newPair.split()) != 2:
        newPair = input("Please enter exactly two floats: ")
    if newPair == "1.0 1.0":
        break
    newPair = newPair.split()
    x = float(newPair[0])
    y = float(newPair[1])
    pt = Point(x, y, "")
    categorize(pt, data, k)






