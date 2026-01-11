import fileSettings

def addWhere(user, where, dict1, dict2):
    subCategoryList = list(dict1["users"][user]["categories"][where].keys())
    while True:
        #i arranca dsd 0 por eso el +1
        for i, subCategory in enumerate(subCategoryList):
            print(f"{i+1}. {subCategory}")
        print(f"{len(subCategoryList)+1}. Add a subCategory...")
        try:
            option = int(input("Choose an option: "))
            if option <1 or option>len(subCategoryList)+1:
                print(f"The option must be between 1-{len(subCategoryList)+1} | Try again")
            elif option == len(subCategoryList)+1:
                newSubCategory = input("Add the new subCategory: ")
                if newSubCategory in subCategoryList:
                    print(f"{newSubCategory} is already a subCategory | Try again")
                else:
                    subCategory = newSubCategory
                    item = input("Write the item's name: ")
                    brand = input("Write the item's brand: ")
                    while True:
                        try:
                            price = int(input("Write the unit item price: "))
                            if price <0:
                                print("The price cannot be below 0 | Try again")
                            else:
                                break
                        except ValueError:
                            print("The price must be a number | Try again")
                    while True:
                        try:
                            quantity = int(input("Write the item's quantity: "))
                            if quantity < 0:
                                print("The quantity cannot be below 0 | Try again")
                            else:
                                break
                        except ValueError:
                            print("The quantity must be a number | Try again")
                    idList = list(dict2["users"][user].keys())
                    newestId = len(idList)
                    newId = newestId+1
                    dict2["users"][user][newId]= {
                        "category": where,
                        "subCategory": subCategory,
                        "item": item,
                        "brand":brand,
                        "unitPrice": price,
                        "quantity": quantity
                    }
                    brandList = []
                    brandList.append(brand)
                    dict1["users"][user]["categories"][where][subCategory][item] = {
                        "brands": brandList
                    }
                    fileSettings.saveFile("expensesFile", dict2)
                    fileSettings.saveFile("usersFile", dict1)
                    return None
                    
            else:
                subCategory = subCategoryList[option-1]
                break
        except ValueError:
            print("The option must be a number | Try again")

    while True:
        itemList = list(dict1["users"][user]["categories"][where][subCategory].keys())
        for i, item in enumerate(itemList):
            print(f"{i+1}. {item}")
        print(f"{len(itemList)+1}. Add an item...")
        try:
            option = int(input("Choose an option: "))
            if option < 1 or option > len(itemList)+1:
                print(f"The option must be between1-{len(itemList)+1} | Try again")
            elif option == len(itemList)+1:
                newItem = input("Write the item's name: ")
                if newItem in itemList:
                    print(f"{newItem} is already a item | Try again")
                else:
                    item = newItem
                    brand = input("Write the item's brand: ")
                    while True:
                        try:
                            price = int(input("Write the unit item price: "))
                            if price <0:
                                print("The price cannot be below 0 | Try again")
                            else:
                                break
                        except ValueError:
                            print("The price must be a number | Try again")
                    while True:
                        try:
                            quantity = int(input("Write the item's quantity: "))
                            if quantity < 0:
                                print("The quantity cannot be below 0 | Try again")
                            else:
                                break
                        except ValueError:
                            print("The quantity must be a number | Try again")
                    idList = list(dict2["users"][user].keys())
                    newestId = len(idList)
                    newId = newestId+1
                    dict2["users"][user][newId]= {
                        "category": where,
                        "subCategory": subCategory,
                        "item": item,
                        "brand":brand,
                        "unitPrice": price,
                        "quantity": quantity
                    }
                    brandList = []
                    brandList.append(brand)
                    dict1["users"][user]["categories"][where][subCategory][item] = {
                        "brands": brandList
                    }
                    fileSettings.saveFile("expensesFile", dict2)
                    fileSettings.saveFile("usersFile", dict1)
                    return None

            else:
                item = itemList[option-1]
                print(item)
                break
        except ValueError:
            print("The option must be a number | Try again")

    brandList = dict1["users"][user]["categories"][where][subCategory][item]["brands"]
    while True:
        for i, brand in enumerate(brandList):
            print(f"{i+1}. {brand}")
        print(f"{len(brandList)+1}. Add a brand...")
        try:
            option = int(input("Choose an option: "))
            if option <1 or option >len(brandList)+1:
                print(f"The option must be between 1-{len(brandList)+1} | Try again")
            elif option == len(brandList)+1:
                newBrand = input("Write the new brand: ")
                if newBrand in brandList:
                    print(f"{newBrand} is already a brand | Try again")
                else:
                    while True:
                        try:
                            price = int(input("Write the unit item price: "))
                            if price <0:
                                print("The price cannot be below 0 | Try again")
                            else:
                                break
                        except ValueError:
                            print("The price must be a number | Try again")
                    while True:
                        try:
                            quantity = int(input("Write the item's quantity: "))
                            if quantity < 0:
                                print("The quantity cannot be below 0 | Try again")
                            else:
                                break
                        except ValueError:
                            print("The quantity must be a number | Try again")
                    idList = list(dict2["users"][user].keys())
                    newestId = len(idList)
                    newId = newestId+1
                    dict2["users"][user][newId]= {
                        "category": where,
                        "subCategory": subCategory,
                        "item": item,
                        "brand":brand,
                        "unitPrice": price,
                        "quantity": quantity
                    }
                    brandList = []
                    brandList.append(brand)
                    dict1["users"][user]["categories"][where][subCategory] = {
                        "brands": brandList
                    }
                    fileSettings.saveFile("expensesFile", dict2)
                    fileSettings.saveFile("usersFile", dict1)
                    return None 
            else:
                brand = brandList[option-1]     
                break              
        except ValueError:
            print("The option must be a number | Try again")

    while True:
        try:
            quantity = int(input("Write the quantity of the item: "))
            if quantity == 0:
                print("The quantity cannot be 0 | Try again")
            else:
                break
        except ValueError:
            print("The option must be a number | Try again")
    while True:
        try:
            price = int(input("Write the unit item price"))
            if price <0:
                print("The price cannot be below 0 | Try again")
            else:
                break
        except ValueError:
            print("The price must be a number | Try again")
    
    idList = list(dict2["users"][user].keys())
    newestId = len(idList)
    newId = newestId+1

    dict2["users"][user][newId] = {
        "category": where,
        "subCategory": subCategory,
        "item": item,
        "brand": brand,
        "quantity": quantity,
        "unitPrice": price
    }
    fileSettings.saveFile("expensesFile", dict2)
    return None


def addExpenseMenu(user, dict1, dict2):
    while True:
        print(f"{'Welcome to the adding an expense menu':-^60}\n1. Add in complex (high involvement)\n2. Add in routine (habitual)\n3. Add in variety seeker (limited comparison)\n4. Add in forced / necessity (captive purchase) \n5. Exit")
        try:
            option = int(input("Choose an option between 1-6: "))
            if option<1 or option>5:
                print("The option must be a number between 1-6 | Try again")
            elif option == 5:
                print("Back to the main menu")
                break
            else:
                match option:
                    case 1:
                        addWhere(user, "complex", dict1, dict2)
                    case 2:
                        addWhere(user, "routine", dict1, dict2)
                    case 3:
                        addWhere(user, "varietySeeking", dict1, dict2)
                    case 4:
                        addWhere(user, "forced", dict1, dict2)
        except ValueError:
            print("The option must be a number | Try again")
    return None