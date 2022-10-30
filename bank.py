def main():
    Input_String = input("Please input the welcome message: ")
    return_Val = value(Input_String)
    print("$" + str(return_Val))


def value(input_string):
    greeting = input_string.strip().lower()
    if greeting.startswith("hello"):
        x = 0
    elif greeting[0] == ("h"):
        x = 20
    else:
        x = 100
    return x


if __name__ == "__main__":
    main()
