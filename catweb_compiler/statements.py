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

            type = block['types'][i]

            if type == "object":
                # arg_value = f"\\u{type}"
                arg_value = chr(int(arg_value))

            new_arg = {
                "value": arg_value,
                "t": type, # Type
                # "l": "?", # Arg name
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
    def __init__(self, inner, times):
        self.inner = inner
        self.times = times

    def compile(self):
        # 23 is repeat forever and 22 is repeat x times
        if int(self.times) < 0:
            start_json = {
                "id": "23", 
                "t": "0",
                "text": [""]
            }
        else:
            start_json = {
                "id": "22", 
                "t": "0",
                "text": ["", {"t": "number", "value": self.times}, ""]
            }

        end_json = {
            "id": "25", # 25 is end
            "t": "0",
            "text": [""]
        }

        all_json = [start_json]
        for statement in self.inner:
            all_json.append(statement.compile())
        all_json.append(end_json)

        return all_json
        
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