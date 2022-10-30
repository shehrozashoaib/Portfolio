def main():
    output_Gauge = convert(input("Please enter the string: "))
    print(gauge(output_Gauge))


def convert(string):
    x, y = string.split("/")
    if not (x.isnumeric() and y.isnumeric()):
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    elif int(x) > int(y):
        raise ValueError
    else:
        return (int(x) / int(y)) * 100


def gauge(integer):
    if integer >= int(99):
        return "F"
    elif integer <= int(1):
        return "E"
    else:
        new_Str = str(int(integer)) + "%"
        return new_Str


if __name__ == "__main__":
    main()