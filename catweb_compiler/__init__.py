from .parser import Parser
from .tokenizer import tokenize

def compile(code: str):
    tokens = tokenize(code)
    parser = Parser(tokens)
    ast = parser.parse()

    actions = []
    for statement in ast.statements:
        action_json = statement.compile()
        actions.append(action_json)

    out_code = [
        {
            "class": "script",
            "content": [
                {
                    "id": "0",
                    "text": [
                        "When website loaded..."
                    ],
                    "actions": actions
                }
            ],
            "globalid": "~"
        }
    ]

    return out_code