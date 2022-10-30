import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(
        r"^<iframe (?:width=[0-9\"]*)? ?(?:height=[0-9\"]*)? ?src=\"https?://(?:www\.)?youtube\.com/embed/(\w+).+",
        s,
    )
    if matches:
        return "https://youtu.be/" + matches.group(1)
        sys.exit()
    return "None"


if __name__ == "__main__":
    main()
