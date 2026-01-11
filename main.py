import fileSettings, userSettings, menu

def main():
    expensesDict = fileSettings.initializeFile("expensesFile")
    userDict = fileSettings.initializeFile("usersFile")
    activeUser = userSettings.userSelectorMenu(userDict, expensesDict)
    if activeUser == -1:
        return None
    else:
        menu.showMenu(activeUser, userDict, expensesDict)
        return None

if __name__ == "__main__":
    main()