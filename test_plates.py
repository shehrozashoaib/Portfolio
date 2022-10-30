from plates import is_valid


def test_min_alpha():
    assert is_valid("AA1233") == True
    assert is_valid("12AA") == False


def test_length():
    assert is_valid("AA1234") == True
    assert is_valid("B") == False
    assert is_valid("DFRT123") == False


def test_order():
    assert is_valid("AA12A0") == False
    assert is_valid("AAB21") == True


def test_alphanumeric():
    assert is_valid("AAS.1") == False
    assert is_valid("BD/12") == False
