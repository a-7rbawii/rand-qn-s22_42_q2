import random

def printList(mylist):
    for x in range(0, 10):
        for y in range(0, 10):
            print(mylist[x][y], " ", end='')
        print("")

mylist = [[0]*10 for i in range(10)]
for x in range(0,10):
    for y in range(0,10):
        mylist[x][y] = random.randint(1,100)
print("Initial Array:")
printList(mylist)

listlength = 10
for X in range(0,listlength):
    for Y in range(0,listlength - 1):
        for Z in range(0,listlength - Y - 1):
            if mylist[X][Y] > mylist[X][Z + 1]:
                Temp = mylist[X][Z]
                mylist[X][Z] = mylist[X][Z + 1]
                mylist[X][Z + 1] = Temp

print("Sorted Array:")
printList(mylist)