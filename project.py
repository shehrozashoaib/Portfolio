import csv


class Party:
    def __init__(self):
        # initialises the two dictionaries
        self.info_attendees = []
        self.detailed_info_attendees = []

    def __str__(self):
        return str(self.info_attendees)

    def add_attendees(self, family_name: str, number_of_attendees: int):
        # adds the information in the dictionary
        self.info_attendees.append(
            {"family_name": family_name, "number_of_attendees": number_of_attendees}
        )

    def detailed_attendees(
        self, family_name: list, adult_attendees: list, child_attendees: list
    ):
        # adds the information in the dictionary
        for i in range(len(family_name)):
            self.detailed_info_attendees.append(
                {
                    "family_name": family_name[i],
                    "adult_attendees": adult_attendees[i],
                    "child_attendees": child_attendees[i],
                }
            )

    def check_and_resolve(self):
        # this method will resolve any discrepancies between the two dictionaries
        # we start resolving by ensuring that the family names in the detailed_info_attendees are also present in the info_attendees dictionary
        family_names = [
            family["family_name"]
            for family in self.detailed_info_attendees
            if not (
                family["family_name"] in (f["family_name"] for f in self.info_attendees)
            )
        ]
        if family_names:
            adult_attendees = [
                family["adult_attendees"]
                for family in self.detailed_info_attendees
                if not (
                    family["family_name"]
                    in (f["family_name"] for f in self.info_attendees)
                )
            ]
            child_attendees = [
                family["child_attendees"]
                for family in self.detailed_info_attendees
                if not (
                    family["family_name"]
                    in (f["family_name"] for f in self.info_attendees)
                )
            ]
            for i in range(len(family_names)):
                self.info_attendees.append(
                    {
                        "family_name": family_names[i],
                        "number_of_attendees": int(adult_attendees[i])
                        + int(child_attendees[i]),
                    }
                )
        # next we make sure that the total number of attendees in each family in detailed_info_attendees correspond to the those in info_attendees
        family_names = [
            family["family_name"]
            for family in self.detailed_info_attendees
            if (
                family["family_name"] in (f["family_name"] for f in self.info_attendees)
            )
        ]
        if family_names:
            adult_attendees = [
                family["adult_attendees"]
                for family in self.detailed_info_attendees
                if (
                    family["family_name"]
                    in (f["family_name"] for f in self.info_attendees)
                )
            ]
            child_attendees = [
                family["child_attendees"]
                for family in self.detailed_info_attendees
                if (
                    family["family_name"]
                    in (f["family_name"] for f in self.info_attendees)
                )
            ]
            for i in range(len(self.info_attendees)):
                try:
                    self.info_attendees[i]["number_of_attendees"] = int(
                        adult_attendees[
                            family_names.index(self.info_attendees[i]["family_name"])
                        ]
                    ) + int(
                        child_attendees[
                            family_names.index(self.info_attendees[i]["family_name"])
                        ]
                    )
                except ValueError:
                    pass

    def get_total_attendees(self):
        # this method will return the total number of attendees
        self.check_and_resolve()
        total = int(0)
        for x in self.detailed_info_attendees:
            v1 = x.get("child_attendees")
            v2 = x.get("adult_attendees")
            total = total + int(v2) + int(v1)
        return total

    def filter_attendees(self):
        # this method will filter out the families in violation of the Covid-19 restrictions
        families = [
            family["family_name"]
            for family in self.detailed_info_attendees
            if (family["child_attendees"] != 0)
            or (
                (int(family["child_attendees"]) + int(family["adult_attendees"]))
                > int(2)
            )
        ]
        return families

    def covid_changes(self):
        # this method will make a text file of families who are in violation of the Covid-19 restrictions
        families = self.filter_attendees()
        with open("families_not_allowed.txt", "w") as file:
            for family in families:
                file.write(
                    "This family cannot come to the party due to Covid-19 restrictions: "
                    + family
                    + "\n"
                )

    def include_priority(self, family_name: list, priority: list):
        # this method will add a new key to the detailed_info_attendees dictionary
        for x in self.detailed_info_attendees:
            i = int(0)
            for family in family_name:
                if x["family_name"] == family:
                    if priority[i] >= int(0) and priority[i] <= int(5):
                        x["priority"] = priority[i]
                i += 1

    def filter_priorities(self, priority: int):
        # this method will return the families whose priority is below the certain threshold
        families = []
        family_names = []
        for family_detail in self.detailed_info_attendees:
            if family_detail.get("priority"):
                families.append(family_detail)
        if families:
            family = filter(lambda s: (s["priority"] <= int(priority)), families)
            for a in family:
                family_names.append(a["family_name"])
        return family_names

    def output_info_attendees(self):
        # this method will create a csv file of the info_attendees dictionary
        with open("info_attendees.csv", "w") as file:
            writer = csv.DictWriter(
                file, fieldnames=["family_name", "number_of_attendees"]
            )
            writer.writeheader()
            for row in self.info_attendees:
                if (
                    row["family_name"] not in self.filter_attendees()
                    and row["family_name"]
                ):
                    writer.writerow(row)

    def output_detailed_info_attendees(self, priority: int):
        # this method will create a csv file of the detailed_info_attendees dictionary
        with open("detailed_info_attendees.csv", "w") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "family_name",
                    "adult_attendees",
                    "child_attendees",
                    "priority",
                ],
            )
            writer.writeheader()
            for row in self.detailed_info_attendees:
                if row["family_name"] not in self.filter_attendees() and row[
                    "family_name"
                ] not in self.filter_priorities(priority):
                    writer.writerow(row)


def main():
    party = Party()
    party.detailed_attendees(
        ["family1", "family2", "family3", "family4"], [2, 1, 4, 5], [0, 1, 2, 0]
    )
    party.add_attendees("family1", 3)
    party.check_and_resolve()
    print(party)
    print(party.filter_attendees())
    party.covid_changes()
    party.include_priority(["family1"], [2])
    print(str(party.get_total_attendees()))
    print(*party.filter_priorities(2))
    party.output_detailed_info_attendees(2)


if __name__ == "__main__":
    main()