import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    return_Time = ""
    matches = re.search(
        r"^([\d]{1,2}):?([\d]{1,2})? (A|P)M to ([\d]{1,2}):?([\d]{1,2})? (A|P)M$", s
    )
    if matches:
        if not (matches.group(2)):
            if int(matches.group(1)) > 12 or int(matches.group(4)) > 12:
                raise ValueError
            if matches.group(3) == "P" and not (matches.group(1) == "12"):
                return_Time = f"{int(matches.group(1)) + 12:02}" + ":00 to "
            elif matches.group(3) == "A" and matches.group(1) == "12":
                return_Time = f"{int(matches.group(1)) - 12:02}" + ":00 to "
            else:
                return_Time = f"{int(matches.group(1)):02}" + ":00 to "
            if matches.group(6) == "P" and not (matches.group(4) == "12"):
                return_Time = return_Time + f"{int(matches.group(4)) + 12:02}" + ":00"
            elif matches.group(6) == "A" and matches.group(4) == "12":
                return_Time = return_Time + f"{int(matches.group(4)) - 12:02}" + ":00"
            else:
                return_Time = return_Time + f"{int(matches.group(4)):02}" + ":00"
            return return_Time
        elif len(matches.groups()) == 6:
            if (
                int(matches.group(1)) > 12
                or int(matches.group(4)) > 12
                or int(matches.group(2)) >= 59
                or int(matches.group(5)) >= 59
            ):
                raise ValueError
            if matches.group(3) == "P" and not (matches.group(1) == "12"):
                return_Time = (
                    f"{int(matches.group(1)) + 12:02}" + ":" + matches.group(2) + " to "
                )
            elif matches.group(3) == "A" and matches.group(1) == "12":
                return_Time = (
                    f"{int(matches.group(1)) - 12:02}" + ":" + matches.group(2) + " to "
                )
            else:
                return_Time = (
                    f"{int(matches.group(1)):02}" + ":" + matches.group(2) + " to "
                )
            if matches.group(6) == "P" and not (matches.group(4) == "12"):
                return_Time = (
                    return_Time
                    + f"{int(matches.group(4)) + 12:02}"
                    + ":"
                    + matches.group(5)
                )
            elif matches.group(6) == "A" and matches.group(4) == "12":
                return_Time = (
                    return_Time
                    + f"{int(matches.group(4)) - 12:02}"
                    + ":"
                    + matches.group(5)
                )
            else:
                return_Time = (
                    return_Time + f"{int(matches.group(4)):02}" + ":" + matches.group(5)
                )
            return return_Time
    else:
        raise ValueError


if __name__ == "__main__":
    main()
