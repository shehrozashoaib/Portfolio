Found = False
MaxIndex = 8
First = 0
Last = MaxIndex - 1
myList = ["" for i in range(8)]
MaxIndexReached = False


def BinarySearch(SearchItem):
    global Last
    global First
    global Found
    global MaxIndexReached
    while not Found and not MaxIndexReached:
        MidPos = (First + Last) // 2
        if myList[MidPos] == int(SearchItem):
            Found = True
        elif myList[MidPos] > int(SearchItem):
            Last = MidPos - 1
        elif myList[MidPos] < int(SearchItem):
            First = MidPos + 1
        elif First >= Last:
            MaxIndexReached = True
        if Found == True:
            print("Location found at ", str(MidPos + 1))
        else:
            print("Location not found")


myList[0] = 8
myList[1] = 12
myList[2] = 52
myList[3] = 68
myList[4] = 75
myList[5] = 83
myList[6] = 98


BinarySearch(12)

print(myList)
