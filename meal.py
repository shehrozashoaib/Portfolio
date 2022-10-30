def main():
    Input_Time = input("Please input the time to confirm the meal type: ")
    Input_Time = Input_Time.strip()
    if convert(Input_Time) >= 7 and convert(Input_Time) <= 8:
        print("breakfast time")
    elif convert(Input_Time) >= 18 and convert(Input_Time) <= 19:
        print("dinner time")
    elif convert(Input_Time) >= 12 and convert(Input_Time) <= 13:
        print("lunch time")


def convert(time):
    if len(time) <= 5:
        x, y = time.split(":")
        z = int(x) + (int(y) / 60)
    else:
        if time[-4:] == "a.m.":
            time = time.rstrip("apm. ")
            x, y = time.split(":")
            z = int(x) + (int(y) / 60)
        elif time[-4:] == "p.m.":
            time = time.rstrip("apm. ")
            x, y = time.split(":")
            if int(x) >= 12:
                x = int(x) - 12
            z = (int(x) + 12) + (int(y) / 60)
    return float(z)


if __name__ == "__main__":
    main()
