
#for testing
#filepath = "C:\Users\lgfit\OneDrive\Desktop\LinuxDevOps\c334-wksrc\user\test.txt"
#keyword = "example"

#open the file
def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

# #actually search
# def search_string(content, keyword):
#     keyword = keyword.lower()
#     content_lower = content.lower()

#     positions = []
#     start = 0
#     while True:
#         pos = content_lower.find(keyword, start)
#         if pos == -1:
#             break
#         positions.append(pos)
#         start = pos + 1

#     return positions

    # content: original raw string
    # tokens: preprocessed tokens 
    # idx: character positions of each token in the original content
    # keyword: word to search for
    # window: number of characters of context to return around each match
   
def search(content: str, tokens: list[str], idx: list[int], keyword: str, window: int = 50) -> list[str]:
    keyword = keyword.lower()
    results = []

    for token, pos in zip(tokens, idx):
        if token == keyword:
            start = max(0, pos - window)
            end = pos + len(keyword) + window
            results.append(content[start:end])

    return results


