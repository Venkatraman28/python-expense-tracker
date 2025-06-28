from flask import Flask, request, jsonify

app = Flask(__name__)
expenses = []

@app.route('/')
def index():
    return "Welcome to Expense Tracker API!"

@app.route('/expenses', methods=['GET'])
def list_expenses():
    return jsonify(expenses)

@app.route('/expenses', methods=['POST'])
def create_expense():
    data = request.json
    if not all(k in data for k in ('description', 'amount', 'category')):
        return jsonify({'error': 'Missing fields'}), 400

    expense = {
        'description': data['description'],
        'amount': float(data['amount']),
        'category': data['category']
    }
    expenses.append(expense)
    return jsonify({'message': 'Expense added'}), 201

@app.route('/totals', methods=['GET'])
def category_totals():
    totals = {}
    for exp in expenses:
        totals[exp['category']] = totals.get(exp['category'], 0) + exp['amount']
    return jsonify(totals)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
