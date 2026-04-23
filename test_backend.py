from backend.main import tokenize, remove_stop, text_preprocess

def test_tokenize():
    assert tokenize("Hello, World!") == ["hello", ",", "world", "!"]
    assert tokenize("This is a test.") == ["this", "is", "a", "test", "."]
    assert tokenize("Multiple   spaces") == ["multiple", "spaces"]
    assert tokenize("New\nLine") == ["new", "\n", "line"]
    assert tokenize("Punctuation!,\"@#") == ["punctuation", "!", ",", "\"", "@", "#"]
    assert tokenize("") == []
    assert tokenize("   ") == []
    assert tokenize("no-punctuation") == ["no", "-", "punctuation"]
    assert tokenize("onething") == ["onething"]
    assert tokenize("Mix oF everything! Does IT work? Yes, iT dOes.") == ["mix", "of", "everything", "!", "does", "it", "work", "?", "yes", ",", "it", "does", "."]

def test_stop():
    assert remove_stop(["the", "cat", "is", "on", "the", "roof"]) == ["cat", "roof"]
    assert remove_stop(["this", "is", "a", "test"]) == ["test"]
    assert remove_stop(["and", "or", "but"]) == []
    assert remove_stop(["hello", "world"]) == ["hello", "world"]
    assert remove_stop([]) == []

def test_text_preprocess():
    assert text_preprocess("Hello, World!") == "hello, world!"
    assert text_preprocess("This is a test.") == "test."
    assert text_preprocess("Multiple   spaces") == "multiple spaces"
    assert text_preprocess("New\nLine") == "new\nline"
    assert text_preprocess("Punctuation!,\"@#") == "punctuation!,\"@#"
    assert text_preprocess("") == ""
    assert text_preprocess("   ") == ""
    assert text_preprocess("no-punctuation") == "no-punctuation"
    assert text_preprocess("Mix oF everything! Does IT work? Yes, iT dOes.") == "mix everything! does work? yes, does."

def file_to_String(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def string_to_file(string, file_path):
    with open(file_path, 'w') as file:
        file.write(string)

def test_file_to_String():
    test_string = "This is a test string."
    test_file_path = "test_path.txt"
    
    string_to_file(test_string, test_file_path)
    
    result = file_to_String(test_file_path)
    
    assert result == test_string
