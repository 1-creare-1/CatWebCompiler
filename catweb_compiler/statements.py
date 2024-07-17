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
        def var_json(name, value):
            return {
                "id": 11, # 11 is set variable to any
                "t": "0",
                "text": [
                    "",
                    {
                        "value": name,
                        "t": "string",
                    },
                    "=",
                    {
                        "value": value,
                        "t": "any",
                    }
                ]
            }
        
        operators = {
            '+': "12",
            "-": "13",
            "*": "14",
            "/": "15",
        }

        if isinstance(self.value, Literal):
            return var_json(self.name, self.value.value)
        else: # BinaryExpression
            if isinstance(self.value.left, Literal):
                left = self.value.left.value
            else: # Identifier
                left = f"{{{self.value.left.value}}}"

            if isinstance(self.value.right, Literal):
                right = self.value.right.value
            else: # Identifier
                right = f"{{{self.value.right.value}}}"

            return [
                var_json(self.name, left),
                {
                    "id": operators[self.value.operator],
                    "t": "0",
                    "text": [
                        "",
                        {
                            "value": self.name,
                            "t": "string",
                        },
                        f"{self.value.operator}",
                        {
                            "value": right,
                            "t": "any",
                        }
                    ]
                },
                
            ]


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
            if i == 0:
                pre = self.name
            else:
                pre = ","
            compiled_args.append(pre)
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
                "text": ["loop"]
            }
        else:
            start_json = {
                "id": "22", 
                "t": "0",
                "text": ["loop (", {"t": "number", "value": self.times}, ")"]
            }

        end_json = {
            "id": "25", # 25 is end
            "t": "0",
            "text": ["end"]
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