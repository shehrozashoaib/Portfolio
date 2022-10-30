import sys


code = []
code_Lines = int(0)
if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments")
elif not (sys.argv[1].endswith(".py")):
    sys.exit("Not a Python file")
else:
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                code.append(line.lstrip().rstrip())
    except FileNotFoundError:
        sys.exit("File does not exist")

for line in code:
    if not (line.startswith("#")) and line.strip():
        code_Lines += 1

print(code_Lines)
