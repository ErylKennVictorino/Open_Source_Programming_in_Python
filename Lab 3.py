"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    LAB 3
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

import LetterGrade

def semesterGrade():
    n = input("How many exams did you take?: ")
    while type(n) != int:
        try:
            n = int(n)
        except ValueError:
            print("The number of exams must be an integer!")
            n = input("How many exams did you take?: ")
    count = 0
    scores = []
    while count < n:
        try:
            e = float(input("what did you get on exam " + str(count + 1) + "?: "))
            if (e >= 0 and e <= 100):
                scores.append(e)
                count += 1
            else:
                print("Your exam grades must be between 0 and 100!")
        except ValueError:
            print("Your exams scores must all be numbers!")
    scores = sorted(scores)
    d = int(input("How many exams were dropped?: "))
    while type(d) != int:
        try:
            d = int(d)
        except ValueError:
            print("The number of exams must be an integer!")
            d = input("How many exams did you take?: ")
    if (d < n):
        scores2 = scores[d:]
        score = (sum(scores2)/len(scores2))
        score = float(score)
        print("Your grade is a " + str(score))
        print("You got an " + LetterGrade.letterGrade(score) + '!')
    else:
        print("The number of grades dropped must be less than the total exams!")
            
semesterGrade()