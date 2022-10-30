condition_Fulfilled = True
month_List = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


while condition_Fulfilled:
    try:
        input_Date = input("Please input the date you want to edit: ")
        if len(input_Date.strip()) <= 10:
            x, y, z = input_Date.strip().split("/")
            if int(x) <= 12:
                if int(y) <= 31:
                    condition_Fulfilled = False
        elif len(input_Date) > 10:
            a, z = input_Date.split(",")
            z = z.strip()
            b, y = a.split()
            try:
                if int(y) <= 31:
                    if b in month_List:
                        index = month_List.index(b)
                        x = int(index) + int(1)
                        condition_Fulfilled = False
            except (NameError, KeyError, ValueError):
                pass
    except (ValueError, NameError, KeyError):
        pass


if len(str(x)) == 1:
    x = "0" + str(x)
if len(y) == 1:
    y = "0" + str(y)

print(str(z), x, y, sep="-")
