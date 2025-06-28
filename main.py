expenses = []

def add_expense(description, amount, category):
    expenses.append({
        'description': description,
        'amount': amount,
        'category': category
    })

def get_expenses():
    return expenses

def get_total_by_category():
    totals = {}
    for exp in expenses:
        totals[exp['category']] = totals.get(exp['category'], 0) + exp['amount']
    return totals
