from project import Party


def test_check_and_resolve():
    party = Party()
    party.detailed_attendees(["hjb", "jhbh", "hbh", "he"], [2, 5, 4, 5], [1, 0, 2, 0])
    party.add_attendees("hjb", 2)
    party.check_and_resolve()
    assert (
        str(party)
        == "[{'family_name': 'hjb', 'number_of_attendees': 3}, {'family_name': 'jhbh', 'number_of_attendees': 5}, {'family_name': 'hbh', 'number_of_attendees': 6}, {'family_name': 'he', 'number_of_attendees': 5}]"
    )


def test_get_total_attendees():
    party = Party()
    party.detailed_attendees(["hjb", "jhbh", "hbh", "he"], [2, 5, 4, 5], [1, 0, 2, 0])
    assert party.get_total_attendees() == 19


def test_filter_attendees():
    party = Party()
    party.detailed_attendees(["hjb", "jhbh", "hbh", "he"], [2, 5, 4, 5], [0, 0, 2, 0])
    assert party.filter_attendees() == ["jhbh", "hbh", "he"]


def test_filter_priority():
    party = Party()
    party.detailed_attendees(["hjb", "jhbh", "hbh", "he"], [2, 5, 4, 5], [1, 0, 2, 0])
    party.include_priority(["hbh"], [2])
    assert party.filter_priorities(2) == ["hbh"]
