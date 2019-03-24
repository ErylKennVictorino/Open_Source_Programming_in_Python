"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    ASSIGNMENT 3
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

"""
1.  Write a program that requests a word (in lower case, or you change it into all lower case for
    processing) as input from the user. You then translate the word into Pig Latin. The rules for
    translating a word into Pig Latin are as follows:
        a. If the word begins with a group of consonants, move them to the end of the word and
        then add ay. For instance, chip becomes ipchay.
        b. If the word begins with a vowel, add way to the end of the word. For instance, else
        becomes elseway.
"""
def pigLatin():
    word = input("Enter a word: ")
    if word.isalpha():
        wordLower = word.lower()
        letters = list(wordLower)
        if (letters[0] in list("aeiou")) or (letters[0] == 'y' and letters[1] not in list("aeiou")):
            print(wordLower + "way")
        else:
            count = 0
            consonants = ''
            while count < len(wordLower):
                if letters[count] not in list("aeiouy"):
                    consonants = consonants + letters[count]
                    count += 1
                else:
                    break
            print(''.join(letters[count:len(wordLower)]) + consonants + "ay")
    else:
        print("Input can only be one word that contains letters from the alphabet.")
        pigLatin()

pigLatin()

"""
2.  Write a program that requests the user to enter an average test score. Check if it is within the
    range of 0 and 100. Request the user’s input again if it is not within the range. The program
    should then evaluate the score and assign a letter grade for display. Make sure that your
    messages to the users are clear and easy to follow. The lookup table for grade assignment is
    as follows:

    Avg. Score (x)  Grade
         x >=90     A
    90 > x >=80     B
    80 > x >=70     C
    70 > x >=60     D
         x < 60     F
"""
def testScore():
    score = input("Enter your grade: ")
    try:
        score = float(score)
        if (score >= 90 and score <= 100):
            print("You got an A!")
        elif (score >= 80 and score < 90):
            print("You got a B!")
        elif (score >= 70 and score < 80):
            print("You got a C!")
        elif (score >= 60 and score < 70):
            print("You got a D!")
        elif (score >= 0 and score < 60):
            print("You got an F!")
        else:
            print("Your grade must be between 0 and 100.")
            testScore()
    except ValueError:
        print("Your grade must be a number.")
        testScore()

testScore()