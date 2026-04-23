PUNCTUATION = [",", ".", "?", "!", "\"", "'", "-", "`", ":", ";", "(", ")", "@", "#", "\n"]
STOP_WORDS = set([
        "the", "is", "in", "and", "to", "of", "a", "that", "it", "with",
        "as", "for", "was", "on", "are", "by", "this", "be", "or",
        "from", "at", "which", "but", "not"
    ])

def tokenize(raw: str) -> list[str]:
    out = []
    token = ""

    def add_token():
        nonlocal token, out

        if token == "":
            return
        out.append(token.lower())
        token = ""

    for c in raw:
        # Skip 's in contractions completely
        if c == "'" and token != "":
            continue
        # Reject spaces, but include punctuation and newlines as their own tokens
        if c in [" "]:
            add_token()
            continue
        elif c in PUNCTUATION:
            add_token()
            out.append(c)
            continue
        
        token += c

    # Add the last token if there is one
    add_token()
        
    return out

def remove_stop(raw: list[str]) -> list[str]: 
    return [token for token in raw if token not in STOP_WORDS]


def text_preprocess(raw: str) -> str:
    out = ""
    tokens = remove_stop(tokenize(raw))
    last_token = None

    # Put a space between each token, but not before punctuation and before/after newlines
    for token in tokens:
        if token in PUNCTUATION or last_token in ["\n", "-"]:
            out += token
        else:
            out += " " + token
        
        last_token = token

    return out.strip()