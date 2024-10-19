class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # 'operator' or 'operand'
        self.left = left  # Left child (Node)
        self.right = right  # Right child (Node)
        self.value = value  # Value for operand nodes (e.g., 'age > 30')

    def __repr__(self):
        return f"Node(type={self.node_type}, value={self.value})"
