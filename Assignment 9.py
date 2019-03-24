"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    ASSIGNMENT 9
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

import pickle

def main():
    presDict = createDictFromBinaryFile("USpresStatesDict.dat")
    state = getState(presDict)
    displayOutput(state, presDict)
   
def createDictFromBinaryFile(fileName):
    try:
        infile = open(fileName, 'rb')
        dictionaryName = pickle.load(infile)
    except (FileNotFoundError, IOError):
        print("The file could not be found, please make sure it is in the right path!")
    else:
        dictionaryName = {}
    finally:
        try:
            infile.close()
        except UnboundLocalError:
            print("The file could not be closed!")

def getState(dictName):
    state = input("Enter the name of a state: ").title()
    print(state)
    try:
        if state in dictName.values():
            return state
        else:
            return "There are no presidents from " + state + '.'
    except AttributeError:
        print("The dictionary is empty!")
    return state

def displayOutput(state, dictName):
    if state.startswith("There"):
        print(state)
    else:
        print("Presidents from", state + ':')
        for pres in sorted(dictName):
            if dictName[pres] == state:
                print("  " + pres[1] + " " + pres[0])

main()