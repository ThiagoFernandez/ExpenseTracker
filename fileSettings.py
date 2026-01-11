import json

def saveFile(fileName, fileVar):
    with open(f"./{fileName}.json", "w") as f:
        json.dump(fileVar, f, indent=4)

def initializeFile(fileName):
    try:
        with open(f"./{fileName}.json", "r") as f:
            fileVar = json.load(f)
            print(f"The {fileName} dict was found")
    except FileNotFoundError:
        print(f"The {fileName} dict was not found")
        fileVar = {"users": {}}
        saveFile(fileName, fileVar)
    except json.JSONDecodeError:
        print(f"The {fileName} dict was empty")
        fileVar = {"users": {}}
        saveFile(fileName, fileVar)

    return fileVar
