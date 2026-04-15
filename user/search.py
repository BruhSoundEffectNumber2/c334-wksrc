
#for testing
#filepath = "C:\Users\lgfit\OneDrive\Desktop\LinuxDevOps\c334-wksrc\user\test.txt"
#keyword = "example"

def search_file(filepath, keyword):
    with open(filepath, "r") as f:
        lines = f.readlines()
    
    results = []
    for line_no, line in enumerate(lines, start=1):
        if keyword.lower() in line.lower():
            results.append((line_no, line.strip()))
    
    return results #return line number and line text

# debug: ask for input
filepath = input("File path: ")
keyword = input("Keyword: ")

results = search_file(filepath, keyword)

if results:
    print(f"\n{len(results)} match(es) found for '{keyword}':\n") #number od ocurences
    for line_no, line in results:
        print(f"  Line {line_no}: {line}")
else:
    print(f"No matches found for '{keyword}'")