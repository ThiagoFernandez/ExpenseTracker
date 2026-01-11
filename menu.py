import userSettings, expensesFunction, removeExpenses, displayFunction
def showMenu(user, dict1, dict2):
    while True:
        print(f"{'Welcome to the main menu':-^60}\n1. Add an expense\n2. Remove an expense\n3. Change expense's category\n4. Display your expenses list\n5. Display your Eisenhower Matrix\n6. Activate/deactivate notifications\n7. User settings\n8. Exit")
        try:
            option = int(input("Choose an option: "))
            if option<1 or option>8:
                print("The option must be a number between 1-8 | Try again")
            elif option ==8:
                print("See you next time")
                break
            else:
                match option:
                    case 1:
                        expensesFunction.addExpenseMenu(user, dict1, dict2)
                    case 2:
                        removeExpenses.removeExpense(user, dict2)
                    case 3:
                        displayFunction.displayExpensesMenu(user, dict2)
                    # case 4:
                    #     displayTendencies(user, dict2):
                    # case 5:
                    #     sendNotifications(user)
                    # case 7:
                    #     result = userSettings.userSettingsMenu(user, dict1, dict2)
                    #     if result == -1:
                    #         return None
        except ValueError:
            print("The option must be a number | Try again")