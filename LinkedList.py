mylist = []
for i in range(10):
    mylist.append([])
    for j in range(2):
        mylist[i].append([])
StartPtr = -1
FreePtr = -1

def Initialise():
    global mylist
    global StartLoc
    global FreePtr
    for i in range(10):
        mylist[i][0] = ""
        mylist[i][1] = i + 1
    mylist[9][1] = -1
    StartLoc = -1
    FreePtr = 0


def InsertItem(NewItem):
    NewItem = NewItem.lower()
    global mylist
    global StartLoc
    global FreePtr
    if FreePtr != -1:
        NewPtr = FreePtr
        mylist[NewPtr][0] = NewItem
        FreePtr = mylist[FreePtr][1]
        ThisPtr = StartLoc
        while ThisPtr != -1 and mylist[ThisPtr][0] < NewItem:
            PreviousPtr = ThisPtr
            ThisPtr = mylist[ThisPtr][1]
        if StartLoc == -1 or mylist[StartLoc][0] > NewItem:
            mylist[NewPtr][1] = StartLoc
            StartLoc = NewPtr
        else:
            mylist[NewPtr][1] = mylist[PreviousPtr][1]
            mylist[PreviousPtr][1] = NewPtr



Initialise()
InsertItem("h")
InsertItem("z")
InsertItem("w")
InsertItem("b")
InsertItem("k")
InsertItem("a")
print(mylist)
print(FreePtr)
