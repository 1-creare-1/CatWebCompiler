import re

# Token types
TOKEN_TYPES = [
    ('NUMBER',   r'\d+'),
    ('STRING',   r'"[^"]*"'),
    # ('STRING',   r'(?<=")[^"]*(?=")'),
    ('IF',       r"if"),
    ('LOOP',     r"loop"),
    ('IDENT',    r'[a-zA-Z_]\w*'),
    ('EQUAL',    r'=='),
    ('ASSIGN',   r'='),

    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('MULTIPLY', r'\*'),
    ('DIVIDE',   r'/'),

    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('LBRACE',   r'\{'),
    ('RBRACE',   r'\}'),
    ('SEMICOLON',r';'),
    ('COMMA',    r','),
    ('WHITESPACE',r'\s+'),
    ('OTHER',    r'.')
]

def remove_comments(code):
    single_line_comment = r'//.*?$'
    multi_line_comment = r'/\*.*?\*/'
    pattern = f'({single_line_comment})|({multi_line_comment})'

    return re.sub(pattern, '', code, flags=re.DOTALL | re.MULTILINE)

def tokenize(code):
    # Remove comments
    code = remove_comments(code)
    tokens = []
    pos = 0
    while pos < len(code):
        match = None
        for token_type, pattern in TOKEN_TYPES:
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                if token_type != 'WHITESPACE':
                    token = (token_type, match.group(0))
                    tokens.append(token)
                pos = match.end(0)
                break
        if not match:
            raise SyntaxError(f'Illegal character at index {pos}')

    # Post processing to remove quotes from strings
    for i, token in enumerate(tokens):
        if token[0] == "STRING":
            tokens[i] = (token[0], token[1][1:-1])
    print(tokens)

    return tokens