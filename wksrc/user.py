from backend import text_preprocess, serialize_preprocess, deserialize_preprocess
from search import search

def file_to_string(file_path: str) -> str:
    """Reads the contents of a file and returns it as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def string_to_file(string: str, file_path: str):
    """Writes a string to a file at the specified path."""
    with open(file_path, 'w') as file:
        file.write(string)

def validate_path(path: str) -> bool:
    """Checks if the provided file path is valid. This does not check if the file exists."""
    if path.strip() == "":
        return False
    
    return path.endswith(".txt")

def pretty_load_file(path: str) -> str:
    """Loads a file and preprocesses its contents with user interaction."""
    print("Loading...")
    try:
        return file_to_string(path)
    except FileNotFoundError:
        print(f"File {path} not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    
    return None

def branch_index(path: str):
    raw = pretty_load_file(path)
    if raw is None:
        return
    print("Indexing...")
    index = text_preprocess(raw)
    print("Saving index...")
    string_to_file(serialize_preprocess(index), path + ".index")
    print(f"Index saved to {path}.index")

def branch_search(path: str):
    raw = pretty_load_file(path)
    index = pretty_load_file(path + ".index")
    if raw is None or index is None:
        return
    try:
        index = deserialize_preprocess(index)
    except TypeError:
        print(f"Index file {path}.index is malformed. Please re-index the file.")
        return
    print("Index loaded.")

    while True:
        try:
            keyword = input("Enter keyword to search: ").strip().lower()
            print(f"Searching for '{keyword}'...")
            results = search(raw, index["tokens"], index["idx"], keyword)

            print(f"Found {len(results)} total results:")
            if len(results) > 0:
                print(results[0])
        except KeyboardInterrupt:
            print("\nExiting.")
            break

def main():
    print("Welcome to the our text indexing and searching system! Please provide a file path to index and search for keywords.")
    print("1) Index a file")
    print("2) Search an indexed file")

    while True:
        branch = input("Enter your choice (1 or 2): ")
        
        if branch in ['1', '2']:
            break

        print("Invalid choice.")

    path = input("Enter file path: ")
    if not validate_path(path):
        print("Invalid file path!")
        return
    
    if branch == '1':
        branch_index(path)
    else:
        branch_search(path)

if __name__ == "__main__":
    main()
