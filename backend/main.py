import nltk

def clean(raw: str) -> str:
    return raw.strip().lower()

def tokenize(raw: str) -> list[str]:
    if not raw or raw.isspace():
        raise ValueError("Input string cannot be empty.")

    return nltk.word_tokenize(raw)

def stem(tokens: list[str]) -> list[str]:
    if not tokens:
        raise ValueError("Input token list cannot be empty.")
    
    porter = nltk.PorterStemmer()
    return [porter.stem(token) for token in tokens]

def text_preprocess(raw: str) -> str:
    final_tokens = stem(tokenize(clean(raw)))

    return ' '.join(final_tokens)