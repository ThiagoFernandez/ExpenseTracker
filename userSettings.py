import pwinput, hashlib, fileSettings
from email_validator import validate_email, EmailNotValidError

def userLogin(dict1, dict2):
    if not dict1["users"]:
        print("Cannot login because there are not a single user yet")
        return userRegister(dict1, dict2)

    usersList = list(dict1["users"].keys())
    while True:
        for i, users in enumerate(usersList):
            print(f"{i+1}. {users}")
        try:
            option = int(input("Select your user: ")) -1 
            if option <0 or option >=len(usersList):
                print(f"The option must be between 1-{len(usersList)} | Try again")
            else:
                while True:
                    checkPassword = pwinput.pwinput(prompt="Write your password: ", mask="*")
                    hashedCheckedPassword = hashlib.sha256(checkPassword.encode("utf-8")).hexdigest()
                    if hashedCheckedPassword == dict1["users"][usersList[option]]["password"]:
                        return usersList[option]
                    else:
                        print("Wrong password | Try again")
        except ValueError:
            print("The option must be a number | Try again")

def userRegister(dict1, dict2):
    while True:
        newUser = input("Write your username: ")
        if newUser in dict1["users"]:
            print(f"The username {newUser} is already in use | Try again")
        else:
            break
    while True:
        newPassword = pwinput.pwinput(prompt="Create a password: ", mask="*")
        checkNewPassword = pwinput.pwinput(prompt="Write it again to confirm: ", mask="*")
        if newPassword == checkNewPassword:
            hashpassword = hashlib.sha256(newPassword.encode("utf-8")).hexdigest()
            while True:
                email = input("Write your email: ")
                try:
                    valid = validate_email(email)
                    print("Valid email:", valid.email)
                    break
                except EmailNotValidError as e:
                    print("Invalid email: ", str(e))
            while True:
                print(f"Enable notifications...\n1. YES\n2. NO")
                try:
                    status = int(input("Choose 1 or 2: "))
                    if status<1 or status>2:
                        print("The option must be between 1-2 | Try again")
                    else:
                        if status == 1:
                            status = True
                        else:
                            status = False
                        break
                except ValueError:
                    print("Your option must be a number | Try again")

            while True:
                try:
                    income = int(input("Write your monthly income/salary: "))
                    break
                except ValueError:
                    print("Your salary/income must be a number | Try again")
            while True:
                try:
                    resetDay = int(input("What day you usually receive it?: "))
                    if resetDay < 1 or resetDay > 31:
                        print("The day must be between 1-31 | Try again")
                    else:
                        break
                except ValueError:
                    print("The day must be a number | Try again")

            dict1["users"][newUser] = {
                "password": hashpassword,
                "email": email,
                "notifications": status,
                "monthlyIncome": income,
                "resetDay": 1,
                "categories": {
                    "routine": {
                        "groceries": {},
                        "fruits": {},
                        "vegetables": {},
                        "meat": {},
                        "dairy": {},
                        "bakery": {},
                        "beverages": {},
                        "snacks": {
                            "potato": {
                                "brands": ["lays", "pringles", "quento"]
                            }
                        },
                        "frozen_food": {},
                        "household": {},
                        "cleaning": {},
                        "personal_care": {},
                        "hygiene": {},
                        "pharmacy": {},
                        "pets": {}
                    },
                    "varietySeeking": {
                        "restaurants": {},
                        "take_away": {},
                        "coffee": {},
                        "fast_food": {},
                        "clothing": {},
                        "shoes": {},
                        "accessories": {},
                        "electronics_small": {},
                        "subscriptions": {},
                        "entertainment": {},
                        "streaming": {},
                        "apps": {},
                        "games": {}
                    },
                    "complex": {
                        "electronics": {},
                        "computer_hardware": {},
                        "software": {},
                        "education": {},
                        "courses": {},
                        "certifications": {},
                        "furniture": {},
                        "appliances": {},
                        "vehicle": {},
                        "health": {},
                        "insurance": {},
                        "travel": {},
                        "real_estate": {}
                    },
                    "forced": {
                        "rent": {},
                        "utilities": {},
                        "electricity": {},
                        "water": {},
                        "gas": {},
                        "internet": {},
                        "mobile_phone": {},
                        "transport": {},
                        "fuel": {},
                        "taxes": {},
                        "fees": {},
                        "medical": {}
                    }
                    }
                    }

            dict2["users"][newUser] = {
                "categories": {
                    "routine":{},
                    "complex": {},
                    "varietySeeking": {},
                    "forced": {}
                }
                }
            fileSettings.saveFile("usersFile", dict1)
            fileSettings.saveFile("expensesFile", dict2)
            return newUser

def deleteUser(user, dict1, dict2):
    while True:
        print(f"Once deleted the user, it cannot be restored\nWrite -1 if you want to go back")
        decision = input("Write your password to delete your user: ") 
        if decision == "-1":
            print("Back to the menu")
            break
        else:
            decisionHashed = hashlib.sha256(decision.encode("utf-8")).hexdigest()
            if decisionHashed == dict1["users"][user]["password"]:
                del dict1["users"][user]
                del dict2["users"][user]
                fileSettings.saveFile("usersFile", dict1)
                fileSettings.saveFile("expensesFile", dict2)
                newActiveUser = userSelectorMenu(dict1, dict2)
                if newActiveUser == None:
                    return -1
                else:
                    break
    return None

def userSelectorMenu(dict1, dict2):
    while True:
        print(f"{'Welcome to the user selector menu':-^60}\n1. Login\n2. Register\n3. Exit")
        try:
            option = int(input("Choose an option: "))
            if option>3 or option <1:
                print("The option must be between 1-3 | Try again")
            elif option == 3:
                print("Closing program...")
                return None
            match option:
                case 1:
                    return userLogin(dict1, dict2)
                case 2:
                    return userRegister(dict1, dict2)
        except ValueError:
            print("The option must be a number | Try again")

def displayUserSettings(user, dict1):
    dict1Display = list(dict1["users"][user].keys())
    for i, setting in enumerate(dict1Display):
        print(f"{i+1}. {setting}:{dict1["users"][user][setting]}")

    return None

def changeWhatSetting(user, what, dict1):
    if what == "password":
        newPassword = pwinput.pwinput(prompt="Write your new password: ", mask="*")
        newHashedPassword = hashlib.sha256(newPassword.encode("utf-8")).hexdigest()
        dict1["users"][user][what]=newHashedPassword
        fileSettings.saveFile("usersFile", dict1)
    else:
        print(f"Remember that if your {what} does not have @gmail.com or alike, the system cannot send you notifications")
        while True:
            newWhat = input(f"Write your new {what}: ")
            try:
                valid = validate_email(newWhat)
                print("Valid email:", valid.email)
                break
            except EmailNotValidError as e:
                print("Invalid email:", str(e))
        
        dict1["users"][user][what] = newWhat
        fileSettings.saveFile("usersFile", dict1)
        print(f"Your {what} has been changed")
    
    return None

def userSettingsMenu(user, dict1, dict2):
    while True:
        print(f"{'Welcome to the user settings menu':-^60}\n1. See your settings\n2. Change your mail\n3. Change your notification status\n4. Change your password\n5. Change your monthly income/salary\n6. Change the monthly reset day\n7. Delete user\n8. Exit")
        try:
            option = int(input("Choose an option: "))
            if option <1 or option>8:
                print("The option must be between 1-8 | Try again")
            elif option == 8:
                print("Back to the menu")
                break
            else:
                match option:
                    case 1:
                        displayUserSettings(user) 
                    case 2:
                        changeWhatSetting(user, "email", dict1)
                    case 3:
                        changeWhatSetting(user,  "notification", dict1)
                    case 4:
                        changeWhatSetting(user,  "password", dict1)
                    case 5:
                        changeWhatSetting(user, "monthlyIncome", dict1)
                    case 6:
                        changeWhatSetting(user, "resetDay", dict1)
                    case 7:
                        result = deleteUser(user, dict1, dict2)
                        if result == -1:
                            return -1
                        
        except ValueError:
            print("The option must be a number | Try again")
    return None