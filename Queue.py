EmptyString = ""
NullPointer = -1
StackSize = 7
Que = ["" for i in range(8)]
TopOfStackPointer = NullPointer
BaseOfStackPointer = NullPointer
Initialised = False


def main():
    enque(50)
    enque(100)
    enque(80)
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
    if not Initialised:
        BaseOfStackPointer = 0
        TopOfStackPointer = 0
        Que[TopOfStackPointer] = ItemtobeInserted
    elif TopOfStackPointer < (StackSize - 1):
        TopOfStackPointer = TopOfStackPointer + 1
        Que[TopOfStackPointer] = ItemtobeInserted
    Initialised = True


def deque():
    global BaseOfStackPointer
    global TopOfStackPointer
    if TopOfStackPointer > BaseOfStackPointer:
        print([BaseOfStackPointer])
        Que[BaseOfStackPointer] = EmptyString
        BaseOfStackPointer = BaseOfStackPointer + 1


main()
