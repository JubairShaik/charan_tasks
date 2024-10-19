 
from flask import Flask, request, jsonify, render_template

from rule_parser import parse_rule
from evaluator import evaluate_ast
from ast_node import Node

app = Flask(__name__)

# Store rules in memory for this simple example
rules = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule():
    """Create a rule and return the AST."""
    rule_string = request.json.get('rule')
    ast = parse_rule(rule_string)
    rule_name = f"rule_{len(rules) + 1}"
    rules[rule_name] = ast
    return jsonify({"rule_name": rule_name, "ast": repr(ast)})

@app.route('/combine_rules', methods=['POST'])
def combine_rules():
    """Combine multiple rules into a single AST."""
    rule_names = request.json.get('rules')
    combined_ast = combine_ast([rules[rule] for rule in rule_names])
    combined_name = f"combined_rule_{len(rules) + 1}"
    rules[combined_name] = combined_ast
    return jsonify({"combined_rule_name": combined_name, "ast": repr(combined_ast)})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    """Evaluate the given rule with the provided data."""
    rule_name = request.json.get('rule')
    user_data = request.json.get('data')
    ast = rules.get(rule_name)
    result = evaluate_ast(ast, user_data)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
