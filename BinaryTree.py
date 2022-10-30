NullPtr = -1
myList = []
for i in range(10):
    myList.append([])
    for j in range(3):
        myList[i].append([])
rootPtr = 0
freePtr = 0

def initialise():
    global rootPtr
    global freePtr
    global myList
    rootPtr = NullPtr
    freePtr = 0
    for i in range(10):
        myList[i][0] = i + 1
    myList[9][0] = NullPtr


def add(NewItem):
    global freePtr
    global myList
    global rootPtr
    NewItem = str(NewItem)
    if freePtr != NullPtr:
        NewPtr = freePtr
        freePtr = myList[freePtr][0]
        myList[NewPtr][1] = NewItem
        myList[NewPtr][0] = NullPtr
        myList[NewPtr][2] = NullPtr
        if rootPtr == NullPtr:
            rootPtr = NewPtr
        else:
            ThisPtr = rootPtr
            while ThisPtr != NullPtr:
                PreviousPtr = ThisPtr
                if myList[ThisPtr][1] > NewItem:
                    TurnLeft = True
                    ThisPtr = myList[ThisPtr][0]
                else:
                    TurnLeft = False
                    ThisPtr = myList[ThisPtr][2]
            if TurnLeft:
                myList[PreviousPtr][0] = NewPtr
            else:
                myList[PreviousPtr][2] = NewPtr


initialise()
add("Lahore")
add("Karachi")
add("Abotabad")
add("Balochistan")
print(rootPtr)
print(my
