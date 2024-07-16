from .parser import Parser
from .tokenizer import tokenize

def flatten(array, new):
    for element in array:
        if isinstance(element, list):
            flatten(element, new)
        else:
            new.append(element)

def compile(code: str):
    tokens = tokenize(code)
    parser = Parser(tokens)
    ast = parser.parse()

    actions = []
    for statement in ast.statements:
        action_json = statement.compile()
        actions.append(action_json)

    # Actions is currently a nested array of actions. Some elements are arrays of more elements while others are just elements themselves.
    # This step flattens everything out
    flat_actions = []
    flatten(actions, flat_actions)

    out_code = [
        {
            "class": "script",
            "content": [
                {
                    "id": "0",
                    "text": [
                        "When website loaded..."
                    ],
                    "actions": flat_actions
                }
            ],
            "globalid": "~"
        }
    ]

    return out_code