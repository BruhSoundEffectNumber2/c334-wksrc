
#for testing
#filepath = "C:\Users\lgfit\OneDrive\Desktop\LinuxDevOps\c334-wksrc\user\test.txt"
#keyword = "example"

#open the file
def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

#actually search
def search_string(content, keyword):
    keyword = keyword.lower()
    content_lower = content.lower()

    positions = []
    start = 0
    while True:
        pos = content_lower.find(keyword, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1

    return positions


# filepath = input("File path: ")
# keyword = input("Keyword: ")

# content = read_file(filepath)
# positions = search_string(content, keyword)

# if positions:
#     print(positions)
# else:
#     print(f"No matches found for '{keyword}'")