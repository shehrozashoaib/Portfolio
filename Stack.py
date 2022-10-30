EmptyString = ""
NullPointer = -1
StackSize = 7
Stack = ["" for i in range(8)]
TopOfStackPointer = -1


def main():
    push(50)
    push(100)
    push(80)
    pop()
    pop()
    push(20)
    push(24)
    push(78)
    pop()
    print(Stack)


def push(ItemtobeInserted):
    global TopOfStackPointer
    if TopOfStackPointer < (StackSize - 1):
        TopOfStackPointer = TopOfStackPointer + 1
        Stack[TopOfStackPointer] = ItemtobeInserted


def pop():
    ItemPrinted = ""
    global TopOfStackPointer
    if TopOfStackPointer > -1:
        ItemPrinted = Stack[TopOfStackPointer]
        Stack[TopOfStackPointer] = EmptyString
        print(ItemPrinted)
        TopOfStackPointer = TopOfStackPointer - 1


main()
