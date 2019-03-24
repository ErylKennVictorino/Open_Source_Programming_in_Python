"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    LAB 2
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

def analyzeNumber():
    num = input("Enter number: ")

    # This checks if the input is a number
    try:
        fl = float(num)
        x = str(abs(fl))
        left, right = x.split(".")
        sizeLeft = len(left)

        #Since we changed the input into a float, if the input was an integer,
        #it would have a zero after the decimal point, so I added this so it
        #doesn't count that as a digit
        if right == "0":
            sizeRight = 0
        else:
            sizeRight = len(right)
            
        # this just changes the word digits to digit if there's only one digit
        if sizeLeft == 1:
            print(str(sizeLeft) + " digit to the left of decimal point")
        else:
            print(str(sizeLeft) + " digits to the left of decimal point")
        if sizeRight == 1:
            print(str(sizeRight) + " digit to the right of decimal point")
        else:
            print(str(sizeRight) + " digits to the right of decimal point")

    #This prints an error if the input isn't a number then calls the function again
    except ValueError:
        print("That is not a valid input.")
        analyzeNumber()
        
analyzeNumber()

def editSentence():
    sentence = input("Enter a sentence: ")
    old = input("Enter word(s) to be replaced: ")
    new = input("Enter replacement word(s): ")
    print(sentence.replace(old, new))

editSentence()