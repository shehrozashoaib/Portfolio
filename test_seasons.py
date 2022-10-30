from seasons import validation

def testing():
    assert validation("2021-07-03") == "Five hundred twenty-five thousand, six hundred minutes"
    assert validation("2020-07-03") == "One million, fifty-one thousand, two hundred minutes"