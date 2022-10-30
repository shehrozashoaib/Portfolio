from twttr import shorten


def test_lowercase():
    assert shorten("hello world") == "hll wrld"
    assert shorten("my name is abc") == "my nm s bc"


def test_uppercase():
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("MY NAME IS ABC") == "MY NM S BC"


def test_charcters_and_num():
    assert shorten("Hello world 123!./") == "Hll wrld 123!./"


def test_lowercase_uppercase_vowels():
    assert shorten("hello wOrld") == "hll wrld"
    assert shorten("mY namE Is abc") == "mY nm s bc"