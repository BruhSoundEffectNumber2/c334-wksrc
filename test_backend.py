from wksrc.backend import tokenize, clean, string_to_file, file_to_String, remove_stop, text_preprocess

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

def test_file_to_String():
    test_string = "This is a test string."
    test_file_path = "test_path.txt"
    
    string_to_file(test_string, test_file_path)
    
    result = file_to_String(test_file_path)
    
    assert result == test_string
