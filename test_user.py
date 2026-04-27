# Needed to import from wksrc without installing it as a package
import sys
sys.path.append("wksrc")
from wksrc.user import validate_path, string_to_file, file_to_string

def test_file_rw():
    test_string = "This is a test string."
    test_file_path = "test_data/dummy.txt"
    
    string_to_file(test_string, test_file_path)
    
    result = file_to_string(test_file_path)
    
    assert result == test_string

def test_validate_path():
    assert validate_path("test_data/dummy.txt") == True
    assert validate_path("nonexistent.txt") == True
    assert validate_path("./test_data/dummy.txt") == True
    assert validate_path("/home/user/test_data/dummy.txt") == True
    assert validate_path("test_data/dummy.doc") == False
    assert validate_path("") == False
    assert validate_path("   ") == False