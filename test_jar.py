from jar import Jar


def test_init():
    jar = Jar()
    assert str(jar) == ""
    assert jar.capacity == 12
    jar = Jar(13)
    assert jar.capacity == 13


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(3)
    assert jar.size == 3
    try:
        jar.deposit(10)
    except ValueError:
        pass


def test_withdraw():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(3)
    assert jar.size == 3
    jar.withdraw(2)
    assert jar.size == 1
    jar.withdraw(1)
    assert jar.size == 0
    try:
        jar.withdraw(10)
    except ValueError:
        pass