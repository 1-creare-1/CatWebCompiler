from .globals_list import globals, get_global

class Node:
    pass

class Program(Node):
    def __init__(self, statements):
        self.statements = statements

class LetStatement(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def compile(self):
        return "let"

class ExpressionStatement(Node):
    def __init__(self, expression):
        self.expression = expression

class CallExpression(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def compile(self):
        block = get_global(self.name)

        if block['args'] != len(self.args):
            print("Uhh yeah this has wrong arg count")
            return

        compiled_args = []
        for i, value in enumerate(self.args):
            compiled_args.append("")
            arg_value = value.value

            new_arg = {
                "value": arg_value,
                "t": "?", # Type
                "l": "?", # Arg name
            }
            print(new_arg)
            compiled_args.append(new_arg)

        return {
            "id": block["id"],
            "t": "0",
            "text": compiled_args
        }


class IfStatement(Node):
    def __init__(self, condition, consequence, alternative):
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative

class Loop(Node):
    def __init__(self):
        self._ =_

    def compile(self):
        ...
        
class BinaryExpression(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class Identifier(Node):
    def __init__(self, value):
        self.value = value

class Literal(Node):
    def __init__(self, value):
        self.value = value