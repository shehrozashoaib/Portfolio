from numb3rs import validate

def test_number_of_sets():
    assert validate("255.255.200") == False
    assert validate("255.255.255.255.255") == False
    assert validate("255.255.255.255") == True


def test_range_of_each_set():
    assert validate("255.255.255.275") == False
    assert validate("255.344.255.2") == False
    assert validate("255.255.255.255") == True


