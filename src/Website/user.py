filename = "Names.txt"
import json

def addName(Players): #parameter user dictionary
    allPlayer = Players #dictionary javascript guy must provide (MUST BE WELL SET)
    with open(filename, "w") as file:
        json.dump(allPlayer, file)

def getNameList(file):
    Users = []
    with open(file) as file:
        for line in file:
            Users.append(line())
    newUsers = json.dump(Users)
    return newUsers




