from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()

if len(sys.argv) == int(3) or len(sys.argv) == int(1):
    l = figlet.getFonts()
    if len(sys.argv) == int(1):
        figlet.setFont(font=choice(tuple(l)))
        print(figlet.renderText(input("Please enter the string: ")))
    if (
        len(sys.argv) == int(3)
        and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
        and l.count(sys.argv[2]) != int(0)
    ):
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(input("Please enter the string: ")))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
