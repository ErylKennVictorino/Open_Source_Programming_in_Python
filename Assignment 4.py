"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    ASSIGNMENT 4
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

"""
1.  Write a program to determine the roots (just the real without the complex) of the quadratic
    equation ax2 + bx + c = 0 (where a != 0) after requesting the values of a, b, and c.
    Before finding the roots, ensure that a is nonzero.
    Note: The equation has 2, 1, or 0 solutions depending on whether the value of b2 – 4ac is
    positive, zero, or negative. The solutions are given by the quadratic formula:
        x = (-b+-sqrt(b^2-4ac))/2a
"""
def realRoots():
    print("Enter the coefficients of a quadratic equation of the form ax^2 + bx + c to find its real roots, where a is nonzero.")
    try:
        a = float(input("What is a?: "))
        if a != 0:
            b = float(input("What is b?: "))
            c = float(input("What is c?: "))
            x1 = ((-b) + (((b**2) - (4*a*c))**(0.5)))/(2*a)
            x2 = ((-b) - (((b**2) - (4*a*c))**(0.5)))/(2*a)
            if (type(x1) == complex or type(x2) == complex):
                print("There is no real solution")
            else:
                if x1 == x2:
                    print("There is one real solution and it is " + str(x1))
                else:
                    print("There are two real solutions and they are " + str(x1) + " , " + str(x2))
        else:
            print("a must be nonzero number!")
            realRoots()
    except ValueError:
        print("a, b and c must all be numbers!")
        realRoots()    

realRoots()

"""
2.  Write a program that requests seven grades as input and then calculates the average after
    dropping the lowest grade. Add in your HW 3 letter grade assignment part and display both the
    average and the letter grade.
"""
def semesterGrade():
    count = 0
    scores = []
    while count < 7:
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
    scores2 = scores[1:]
    score = (sum(scores2)/len(scores2))
    score = float(score)
    print(score)
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

semesterGrade()