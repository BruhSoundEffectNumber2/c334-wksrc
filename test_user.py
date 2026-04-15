from user import hello
from backend import text_preprocess, file_to_String, string_to_file

def test_main():
    assert hello() == "Hello, World!"
