from datetime import date, datetime
import inflect
import sys

p = inflect.engine()


def main():
    print(validation(input("Date of birth: ")))


def validation(t1):
    try:
        x = lambda s: bool(datetime.strptime(s, "%Y-%m-%d"))
        if x(t1):
            t1 = date.fromisoformat(t1)
            t2 = date.today()
            t3 = t2 - t1
            output_int = int(t3.total_seconds() / 60)
            output_str = p.number_to_words(output_int)
            output_str = output_str.replace(" and", "").capitalize() + " minutes"
            return output_str
    except ValueError:
        sys.exit("Invalid input format")


if __name__ == "__main__":
    main()
