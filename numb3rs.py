import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^([0-9]{0,3})\.([0-9]{0,3})\.([0-9]{0,3})\.([0-9]{0,3})$", ip)
    if matches:
        if (
            int(matches.group(1)) >= 0
            and int(matches.group(1)) <= 255
            and int(matches.group(2)) >= 0
            and int(matches.group(2)) <= 255
            and int(matches.group(3)) >= 0
            and int(matches.group(3)) <= 255
            and int(matches.group(4)) >= 0
            and int(matches.group(4)) <= 255
        ):
            return True
            sys.exit()
    return False


if __name__ == "__main__":
    main()
