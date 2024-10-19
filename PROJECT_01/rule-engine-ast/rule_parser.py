import re
from ast_node import Node

def parse_rule(rule_string):
    """Parse a rule string and build an AST."""
    tokens = re.split(r'(\s+AND\s+|\s+OR\s+)', rule_string)
    stack = []

    for token in tokens:
        token = token.strip()
        if token == 'AND' or token == 'OR':
            # Pop two operands and push them with an operator
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(node_type='operator', left=left, right=right, value=token))
        else:
            # Operand (e.g., 'age > 30')
            stack.append(Node(node_type='operand', value=token))

    return stack[0]  # The final node in the stack should be the root of the AST
