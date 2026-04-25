import json

PUNCTUATION = [",", ".", "?", "!", "\"", "-", "`", ":", ";", "(", ")", "@", "#", "\n"]
STOP_WORDS = set([
        "the", "is", "in", "and", "to", "of", "a", "that", "it", "with",
        "as", "for", "was", "on", "are", "by", "this", "be", "or",
        "from", "at", "which", "but", "not"
    ])

def tokenize(raw: str) -> tuple[list[str], list[int]]:
    out = ([], [])
    token = ""
    token_start = 0

    def add_token():
        nonlocal token, out, token_start

        if token == "":
            return
        out[0].append(token.lower())
        out[1].append(token_start)
        token = ""

    for idx, c in enumerate(raw):
        # Skip 's in contractions completely
        if c == "'" and token != "":
            continue
        # Reject spaces, but include punctuation and newlines as their own tokens
        if c in [" "]:
            add_token()
            continue
        elif c in PUNCTUATION:
            add_token()
            out[0].append(c)
            out[1].append(idx)
            continue
        
        if token == "":
            token_start = idx
        token += c

    # Add the last token if there is one
    add_token()
        
    return out

def remove_stop(raw: tuple[list[str], list[int]]) -> tuple[list[str], list[int]]: 
    out = ([], [])

    for i in range(len(raw[0])):
        if raw[0][i] not in STOP_WORDS:
            out[0].append(raw[0][i])
            out[1].append(raw[1][i])

    return out

def serialize_preprocess(pre: tuple[list[str], list[int]]) -> str:
    return json.dumps({"tokens": pre[0], "idx": pre[1]})

def deserialize_preprocess(pre_str: str) -> tuple[list[str], list[int]]:
    pre_dict = json.loads(pre_str)
    return (pre_dict["tokens"], pre_dict["idx"])

def text_preprocess(raw: str) -> dict:
    final = remove_stop(tokenize(raw))
    return {"tokens": final[0], "idx": final[1]}

def file_to_String(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def string_to_file(string, file_path):
    with open(file_path, 'w') as file:
        file.write(string)
