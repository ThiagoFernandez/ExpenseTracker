import fileSettings

def removeExpense(user, dict2):
    user_expenses = dict2["users"].get(user, {})
    expense_ids = list(user_expenses.keys())

    if not expense_ids:
        print("No expenses to delete.")
        return None

    while True:
        for i, exp_id in enumerate(expense_ids, start=1):
            print(f"{i}. {user_expenses[exp_id]['name']}")
        print(f"{len(expense_ids)+1}. Back to the menu")

        try:
            option1 = int(input("Choose an option: "))
            if option1 < 1 or option1 > len(expense_ids) + 1:
                print(f"The option must be between 1-{len(expense_ids)+1} | Try again")
                continue

            if option1 == len(expense_ids) + 1:
                return None

            chosen_id = expense_ids[option1 - 1] 
            expense = user_expenses[chosen_id]

            print("Is this the expense you want to delete?")
            for k, v in expense.items():
                if k != "name":
                    print(f" - - -\n{k}: {v}")
            print(f" - - -\n1. Yes\n2. No")

            try:
                option2 = int(input("Choose an option: "))
                if option2 == 1:
                    del user_expenses[chosen_id]
                    fileSettings.saveFile("expensesFile", dict2)
                    return None
                elif option2 == 2:
                    continue
                else:
                    print("The option must be between 1-2 | Try again")
            except ValueError:
                print("The option must be a number | Try again")

        except ValueError:
            print("The option must be a number | Try again")
