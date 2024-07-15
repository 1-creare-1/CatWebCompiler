from .tokenizer import tokenize
from .statements import *


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            statements.append(self.parse_statement())
        return Program(statements)

    def parse_statement(self):
        if self.match('IDENT', "ASSIGN"):
            return self.parse_let_statement()
        elif self.match('IF'):
            return self.parse_if_statement()
        elif self.match('IDENT', 'LPAREN'):
            return self.parse_call()
        else:
            raise SyntaxError(f'Unexpected token: {self.tokens[self.pos]}')

    def parse_let_statement(self):
        name = self.consume('IDENT')
        self.consume('ASSIGN')
        value = self.parse_expression()
        self.consume('SEMICOLON')
        return LetStatement(name, value)

    def parse_expression_statement(self):
        expr = self.parse_expression()
        self.consume('SEMICOLON')
        return ExpressionStatement(expr)

    def parse_if_statement(self):
        self.consume('IF')
        self.consume('LPAREN')
        condition = self.parse_expression()
        self.consume('RPAREN')
        self.consume('LBRACE')
        consequence = []
        while not self.match('RBRACE'):
            consequence.append(self.parse_statement())
        self.consume('RBRACE')
        alternative = None
        if self.match('ELSE'):
            self.consume('ELSE')
            self.consume('LBRACE')
            alternative = []
            while not self.match('RBRACE'):
                alternative.append(self.parse_statement())
            self.consume('RBRACE')
        return IfStatement(condition, consequence, alternative)

    def parse_call(self):
        name = self.consume('IDENT')
        self.consume('LPAREN')
        args = []
        while not self.match("RPAREN", "SEMICOLON"):
            arg = self.parse_primary()
            args.append(arg)
            if self.look_ahead(1) == "SEMICOLON":
                break
            self.consume("COMMA")

        self.consume('RPAREN')
        self.consume('SEMICOLON')
       
        return CallExpression(name, args)
    
    def parse_expression(self):
        left = self.parse_primary()
        if self.match('PLUS'):
            operator = self.consume('PLUS')
            right = self.parse_primary()
            return BinaryExpression(left, operator, right)
        return left

    def parse_primary(self):
        if self.match('NUMBER'):
            return Literal(self.consume('NUMBER'))
        elif self.match('STRING'):
            return Literal(self.consume('STRING'))
        elif self.match('IDENT'):
            return Identifier(self.consume('IDENT'))
        elif self.match('LPAREN'):
            self.consume('LPAREN')
            expr = self.parse_expression()
            self.consume('RPAREN')
            return expr
        else:
            raise SyntaxError(f'Unexpected token: {self.tokens[self.pos]}')

    def match(self, *token_types):
        return all(self.tokens[self.pos + i][0] == token_type for i, token_type in enumerate(token_types))

    def look_ahead(self, n):
        return self.tokens[self.pos + n][0] if self.pos + n < len(self.tokens) else None

    def consume(self, token_type):
        if self.tokens[self.pos][0] == token_type:
            token = self.tokens[self.pos]
            self.pos += 1
            return token[1]
        else:
            raise SyntaxError(f'Expected {token_type}, got {self.tokens[self.pos][0]}')

# Example usage
# code = '''x = 10;
# y = 15;
# sum = x + y;
# log("hello, world");
# log("Sum is: {sum}");
# wait(3);
# log("time has passed");

# if (sum == 100) {
#     log("Sum is 100");
# } else {
#     log("Sum isn't 100");
# }'''
# code = 'x=10;y=20;'
