import sys
import csv


students = []
headers = []
i = int(1)
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not (sys.argv[1].endswith(".csv")) or not (sys.argv[2].endswith(".csv")):
    sys.exit("Not a Python file")
else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                first_name, last_name = row["name"].split(",")
                students.append(
                    {
                        "first_name": first_name.strip(),
                        "last_name": last_name.strip(),
                        "house": row["house"],
                    }
                )
    except FileNotFoundError:
        sys.exit("File does not exist")

students = sorted(students, key=lambda d: d["first_name"])

with open(sys.argv[2], "a") as file:
    writer = csv.DictWriter(file, fieldnames=["first_name", "last_name", "house"])
    writer.writeheader()
    writer.writerows(students)
