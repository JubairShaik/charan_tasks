document.getElementById('create-rule-button').addEventListener('click', async () => {
    const ruleString = document.getElementById('rule-input').value;
    const response = await fetch('/create_rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rule: ruleString })
    });
    const result = await response.json();
    document.getElementById('rule-output').innerText = `Rule Created: ${result.rule_name}, AST: ${result.ast}`;
});

document.getElementById('evaluate-rule-button').addEventListener('click', async () => {
    const ruleName = document.getElementById('rule-input').value;  // Assuming you have a way to input/select the rule name
    const dataInput = document.getElementById('data-input').value;

    // Parse the user data input
    let userData;
    try {
        userData = JSON.parse(dataInput);
    } catch (error) {
        alert("Invalid JSON format in data input.");
        return;
    }

    const response = await fetch('/evaluate_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            rule: ruleName,
            data: userData,
        }),
    });

    const result = await response.json();
    const outputDiv = document.getElementById('evaluation-output');

    if (response.ok) {
        outputDiv.textContent = `Evaluation Result: ${result.result}`;
    } else {
        outputDiv.textContent = `Error: ${result.error}`;
    }
});
