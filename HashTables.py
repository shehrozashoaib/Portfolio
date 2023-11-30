myList = []
for i in range(10):
    myList.append({"StID": -1, "StName": ""})


def AddRecord(StNameI, StIDI):
    StIDI = int(StIDI)
    Full = False
    x = lambda a: a % 10
    index = x(StIDI)
    tempIndex = index
    global myList
    while True:
        if myList[index]["StID"] != -1:
            index+=1
            if index == 9:
                index = 0
            elif tempIndex == index:
                full = True
                break
    if not Full:
        myList[index].update({"StID": StIDI, "StName": StNameI})
    else:
        print("Array is full")
        

def FindRecord(StIDI):
    x = lambda a: a % 10
    index = x(StIDI)
    temp = index
    found = False
    global myList
    while True:
        if myList[index]["StID"] == StIDI:
            print("Record found at ", str(index))
            break
        elif not found:
            index = index + 1
            if myList[index]["StID"] == StIDI:
                print("Record found at ", str(index))
                break
            if index == 9:
                index = 0
        else: 
            print("Record not found")
    
        
    

AddRecord("Shehroz", 12)
AddRecord("Ahmad", 15)
AddRecord("Shoaib",12)
print(myList)
