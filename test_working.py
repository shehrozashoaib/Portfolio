from working import convert
import sys

def test_format1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:25 AM to 5:00 PM") == "09:25 to 17:00"

def test_format2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("11 AM to 11 PM") == "11:00 to 23:00"

def test_order():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_out_of_range():
    try:
        assert convert("9:60 AM to 15:60 PM")
        assert convert("9:60 AM 5:60 PM")
    except ValueError:
        SystemExit


def test_wrong_format():
    try:
        assert convert("9 AM - 5 PM")
    except ValueError:
        SystemExit