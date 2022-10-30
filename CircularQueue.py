EmptyString = ""
NullPointer = -1
StackSize = 8
Que = ["" for i in range(8)]
TopOfStackPointer = NullPointer
BaseOfStackPointer = NullPointer
Initialised = False
ItemsAdded = 0


def main():
    enque(50)
    enque(100)
    enque(80)
    enque(21)
    enque(30)
    enque(84)
    enque(14)
    deque()
    deque()
    enque(20)
    enque(24)
    enque(78)
    deque()
    print(Que)


def enque(ItemtobeInserted):
    global TopOfStackPointer
    global BaseOfStackPointer
    global Initialised
    global ItemsAdded
    global Que
    if not Initialised:
        BaseOfStackPointer = 0
        TopOfStackPointer = 0
        Que[TopOfStackPointer] = ItemtobeInserted
        ItemsAdded += 1
    elif ItemsAdded < 8:
        if TopOfStackPointer < (StackSize - 1):
            TopOfStackPointer = TopOfStackPointer + 1
        elif TopOfStackPointer == (7):
            TopOfStackPointer = 0
        Que[TopOfStackPointer] = ItemtobeInserted
        ItemsAdded += 1
    Initialised = True


def deque():
    global BaseOfStackPointer
    global TopOfStackPointer
    global ItemsAdded
    global Que
    if ItemsAdded > 0:
        print(Que[BaseOfStackPointer])
        Que[BaseOfStackPointer] = EmptyString
        ItemsAdded -= 1
        if ItemsAdded == 0:
            TopOfStackPointer = NullPointer
            BaseOfStackPointer = NullPointer
            ItemsAdded = 0
        else:
            BaseOfStackPointer = BaseOfStackPointer + 1
            if BaseOfStackPointer > 6:
                BaseOfStackPointer = 0


main()
print(Que)
