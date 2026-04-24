from user.main import hello
from user.search import search_string

def test_main():
    assert hello() == "Hello, World!"

def test_search_string():
    content = "This is an example line. Another example here. No match on this line."
    keyword = "example"

    assert search_string(content, keyword) == [11, 33]
