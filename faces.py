def main():
    InputString= input("Please input the string you want to modify? ")
    Modify(InputString)


def Modify(ModifiedString):
    ModifiedString = ModifiedString.replace(":)","🙂")
    ModifiedString = ModifiedString.replace(":(","🙁")
    print(ModifiedString)
    return ModifiedString

main()