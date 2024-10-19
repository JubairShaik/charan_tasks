import re

def evaluate_ast(node, data):
    """Evaluate the AST recursively against the user data."""
    if node is None:
        raise ValueError("Node is None, cannot evaluate AST")
    if node.node_type == 'operand':
        # Evaluate condition like 'age > 30'
        attribute, operator, value = parse_operand(node.value)
        return eval(f"{data.get(attribute)} {operator} {value}")
    
    elif node.node_type == 'operator':
        # Evaluate the left and right child with AND/OR logic
        if node.value == 'AND':
            return evaluate_ast(node.left, data) and evaluate_ast(node.right, data)
        elif node.value == 'OR':
            return evaluate_ast(node.left, data) or evaluate_ast(node.right, data)

def parse_operand(value):
    if not value:
        return None  # or raise an exception
    # Example logic
    # Split value into parts, return them as a tuple
    parts = value.split(' ')  # Example splitting logic
    if len(parts) != 3:
        return None  # Ensure you have exactly 3 parts
    return parts[0], parts[1], parts[2]  # attribute, operator, value
