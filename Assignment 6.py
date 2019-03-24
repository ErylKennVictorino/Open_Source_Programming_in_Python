"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    ASSIGNMENT 6
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

"""
1.  Write a program that asks the user to input a positive integer and then calculates and displays
    the factorial of the number. The factorial of a positive integer n (written n!) is the product of
    1 * 2 * 3 …* n. The program should call a function named getN that gets the user
    input and guarantees that the input is a positive integer. Also, the factorial of the number
    input should be calculated with a function named fact. Use a main function so other
    functions can be invoked from there.
"""
def main1():
    n = getN()
    f = fact(n)
    print("The factorial of " + str("{0:,d}".format(n)) + " is " + str("{0:,d}".format(f)))

def getN():
    n = ''
    while type(n) != int:
        n = input("Please enter a positive integer: ")
        try:
            nInt = int(n)
            if (nInt > 0):
                return nInt
            else:
                print("You must enter a positive integer!")
        except ValueError:
            print("You must enter an integer!")

def fact(n):
    f = n
    count = n - 1
    while count > 0:
        f = f * count
        count -= 1
    return f

main1()

"""
2.  Write a pay-raise program that requests a person’s first name, last name, and current annual
    salary, and then displays the person’s full name and salary for next year. Individuals’ earning
    less than $40,000 will receive a 5% raise, and those earning $40,000 or more will receive a
    raise of $2,000 plus 2% of the amount over $40,000. The main function should call three
    functions – one (multi-valued) for input, one to calculate the new salary, and one for output.
"""
def main2():
    fName, lName, salary = getInfo()
    newSalary = payRaise(salary)
    outputNewInfo(fName, lName, newSalary)

def getInfo():
    fName = input("Please enter your first name: ")
    salary = ''
    while (all(i.isalpha() for i in fName.split('-')) == False):
        print("Your first name must only contain letters! (hyphens allowed).")
        fName = input("Please enter your first name: ")
    lName = input("Please enter your last name: ")
    while (all(j.isalpha() for j in lName.split('-')) == False):
        print("Your last name must only contain letters! (hyphens allowed).")
        lName = input("Please enter your last name: ")
    while (type(salary) != float):
        salary = input("Please enter your current salary: ")
        salary = salary.replace('$', '').replace(',', '')
        try:
            fl = float(salary)
            if (fl >= 0):
                salary = fl
            else:
                print("Your salary cannot be negative!")
        except ValueError:
            print("Your salary must be a number!")
    return (fName, lName, salary)

def payRaise(salary):
    if (salary < 40000):
        newSalary = salary*1.05
    else:
        newSalary = salary + 2000 + (salary - 40000)*0.02
    return newSalary

def outputNewInfo(fName, lName, newSalary):
    fullName = [fName.title(), lName.title()]
    print(' '.join(fullName) + "'s salary for next year is " +
          "${0:,.2f}".format(newSalary))

main2()