from backend.main import hello

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

def test_main():
    assert hello() == "Hello, World!"