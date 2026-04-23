from backend import text_preprocess, file_to_String, string_to_file
def hello():
    return "Hello, World!"

def given_path(path):
    # validate the file path 
    try:        
        with open(path, 'r') as file:
            print(f"File {path} successfully opened. Proceeding with indexing and searching.")
            # Add other functions for indexing here
            text = file_to_String(path)
            Processed = text_preprocess(text)
            print(f"Original text: {text}")
            print(f"Processed text: {Processed}")
            string_to_file(Processed, "processed_output.txt")

    except FileNotFoundError:
        print(f"File {path} not found. Please check the file path and try again.")

if __name__ == "__main__":
    print(hello())
    print("Welcome to the our text indexing and searching system! Please provide a file path to index and search for keywords.")
    path = input("Enter file path: ")
    print(f"File path entered: {path} Is this correct? (y/n)")
    confirmation = input().lower()
    if confirmation == 'y':
        print(f"File path {path} confirmed. Proceeding with indexing and searching.")
        given_path(path)
    else:        print("File path not confirmed. Please restart the program and enter the correct file path.")
