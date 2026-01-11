import fileSettings

def removeExpense(user, dict2):
    expenseList = list(dict2["users"][user].keys())
    while True:
        for i, expense in enumerate(expenseList):
            expenseSections = list(dict2["users"][user][expense])
            for j, section in enumerate(expenseSections):
                print(f"{i+1}.{j+1}). {section}:{dict2["users"][user][expense][section]}")
        break
    return None