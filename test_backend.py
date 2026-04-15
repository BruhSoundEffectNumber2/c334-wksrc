import pytest

from backend.main import tokenize, clean, stem

def test_clean():
    assert clean("  Hello, World!  ") == "hello, world!"
    assert clean("\nNew Line\n") == "new line"
    assert clean("Mixed CASE") == "mixed case"
    assert clean("Special chars!@#") == "special chars!@#"
    assert clean("") == ""
    assert clean("   ") == ""
    assert clean("12345") == "12345"
    assert clean("In the\nmiddle") == "in the\nmiddle"

def test_tokenize():
    # Basic test cases
    assert tokenize("Hello, World!") == ["Hello", ",", "World", "!"]
    assert tokenize("This is a test.") == ["This", "is", "a", "test", "."]

    # Error handling
    with pytest.raises(ValueError):
        tokenize("")
        tokenize("   ")

def test_stem():
    assert stem(["running", "jogged", "happily"]) == ["run", "jog", "happili"]
    assert stem(["cats", "dogs", "mice"]) == ["cat", "dog", "mice"]
    assert stem(["happier", "happiest"]) == ["happier", "happiest"]

    # Some more difficult cases
    assert stem(["lying"]) == ["lie"]
    assert stem(["studies"]) == ["studi"]
    assert stem(["flying"]) == ["fli"]

    # Cases where it does not work quite right
    assert stem(["women"]) == ["women"]  # Not "woman"

    # No change cases
    assert stem(["run"]) == ["run"]
    assert stem(["foo"]) == ["foo"]
    assert stem(["hello", "world"]) == ["hello", "world"]