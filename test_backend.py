from wksrc.backend import *

def test_tokenize():
    assert tokenize("Hello, World!") == (["hello", ",", "world", "!"], [0, 5, 7, 12])
    assert tokenize("This is a test.") == (["this", "is", "a", "test", "."], [0, 5, 8, 10, 14])
    assert tokenize("Multiple   spaces") == (["multiple", "spaces"], [0, 11])
    assert tokenize("New\nLine") == (["new", "\n", "line"], [0, 3, 4])
    assert tokenize("Punctuation!,\"@#") == (["punctuation", "!", ",", "\"", "@", "#"], [0, 11, 12, 13, 14, 15])
    assert tokenize("") == ([], [])
    assert tokenize("   ") == ([], [])
    assert tokenize("no-punctuation") == (["no", "-", "punctuation"], [0, 2, 3])
    assert tokenize("onething") == (["onething"], [0])
    assert tokenize("Mix oF everything! Does IT work? Yes, iT   dOes.") == (["mix", "of", "everything", "!", "does", "it", "work", "?", "yes", ",", "it", "does", "."], [0, 4, 7, 17, 19, 24, 27, 31, 33, 36, 38, 43, 47])

def test_stop():
    assert remove_stop((["the", "cat", "is", "on", "the", "roof"], [0, 5, 8, 11, 15, 19])) == (["cat", "roof"], [5, 19])
    assert remove_stop((["this", "is", "a", "test"], [0, 5, 8, 10])) == (["test"], [10])
    assert remove_stop((["and", "or", "but"], [0, 4, 7])) == ([], [])
    assert remove_stop((["hello", "world"], [0, 6])) == (["hello", "world"], [0, 6])
    assert remove_stop(([], [])) == ([], [])

def test_text_preprocess():
    assert text_preprocess("Hello, World!") == {"idx": [0, 5, 7, 12], "tokens": ["hello", ",", "world", "!"]}
    assert text_preprocess("This is a test.") == {"idx": [10, 14], "tokens": ["test", "."]}
    assert text_preprocess("Multiple   spaces") == {"idx": [0, 11], "tokens": ["multiple", "spaces"]}
    assert text_preprocess("New\nLine") == {"idx": [0, 3, 4], "tokens": ["new", "\n", "line"]}
    assert text_preprocess("Punctuation!,\"@#") == {"idx": [0, 11, 12, 13, 14, 15], "tokens": ["punctuation", "!", ",", "\"", "@", "#"]}
    assert text_preprocess("") == {"idx": [], "tokens": []}
    assert text_preprocess("   ") == {"idx": [], "tokens": []}
    assert text_preprocess("no-punctuation") == {"idx": [0, 2, 3], "tokens": ["no", "-", "punctuation"]}
    assert text_preprocess("Mix oF everything! Does IT work? Yes,   iT dOes.") == {"idx": [0, 7, 17, 19, 27, 31, 33, 36, 43, 47], "tokens": ["mix", "everything", "!", "does", "work", "?", "yes", ",", "does", "."]}

def test_serialize_deserialize():
    pre = (["hello", "world"], [0, 6])
    pre_str = serialize_preprocess(pre)
    assert deserialize_preprocess(pre_str) == pre

    pre = (["more", "complex", "test", "!"], [0, 5, 12, 22])
    pre_str = serialize_preprocess(pre)
    assert deserialize_preprocess(pre_str) == pre

    pre = ([], [])
    pre_str = serialize_preprocess(pre)
    assert deserialize_preprocess(pre_str) == pre

def test_file_to_String():
    test_string = "This is a test string."
    test_file_path = "test_path.txt"
    
    string_to_file(test_string, test_file_path)
    
    result = file_to_String(test_file_path)
    
    assert result == test_string
