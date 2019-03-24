"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    ASSIGNMENT 5
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

"""
1.  Write a program to calculate the monthly mortgage payment when buying a house. You
    should have a function that takes 3 parameters, P, r, and n. Calculate the monthly payment
    and return it to the caller. The equation is:
        M= P*(r*((1+r)^n))/(((1+r)^n)-1)
    and each variable represents the following:
        • P is the principal, the money you borrowed from the bank,
        • r is your monthly interest rate, calculated by dividing your annual interest rate by 12,
        • n is your number of payments (the number of months you will be paying the loan)
    You need to get user input for amount of the money she/he borrowed from the bank, annual
    interest rate, and number of years of the loan. Make necessary calculation before calling and
    passing the values to the function. Display all 4 values, principal, annual interest rate, loan
    period in years, and the monthly payment to the screen. Use proper format for each value
    when display them.
"""
def main():
    P, r_annual, n_years = getInfo()
    M = monthlyPayments(P, r_annual, n_years)
    outputData(P, r_annual, n_years, M)

def getInfo():
    P = ''
    r_annual = ''
    n_years = ''
    while (type(P) != float):
        try:
            P = float(input("Enter the principal: ").replace('$', '').replace(',', ''))
            if P >= 0:
                while (type(r_annual) != float):
                    try:
                        r_annual = float(input("Enter the annual interest rate (percent form):").replace('%', ''))
                        if r_annual >= 0:
                            while (type(n_years) != int):
                                try:
                                    n_years = int(input("Enter the number of years: ").replace(',', ''))
                                    if n_years > 0:
                                        return (P, r_annual, n_years)
                                    else:
                                        print("The number of years must be positive!")
                                        n_years = ''
                                except ValueError:
                                    print("The number of years must be a positive integer!")
                        else:
                            print("The annual interest rate must be non-negative!")
                            r_annual = ''
                    except ValueError:
                        print("The annual interest rate must be a non-negative number!")
            else:
                print("The principal must be non-negative!")
                P = ''
        except ValueError:
            print("The principal must be a non-negative number!")

def monthlyPayments(P, r_annual, n_years):
    r = (r_annual/12)/100
    n = n_years*12
    d = ((1+r)**n)
    if (d > 1):
        M = (P*r*d)/(d-1)
    else:
        M = P/n
    return M

def outputData(P, r_annual, n_years, M):
    print("the principal is " + '${0:,.2f}'.format(P))
    print("the annual interest rate is " + '{0:,.2%}'.format(r_annual/100))
    print("the loan period is " + '{0:,d}'.format(n_years) + " years")
    print("the monthly payment is " + '${0:,.2f}'.format(M))
    

main()

"""
2.  Create a text file and name it planets.txt that includes all planets (Mercury, Venus,
    Mars, Earth, Jupiter, Neptune, Saturn, Uranus).
    Write a program that reads in the file and populates all planets into a list, sorts the list, and
    display the first 5 planets in the list.
"""
def sortPlanets():
    planets = []
    infile = open("planets.txt", 'r')
    for line in infile:
        planets.append(line.strip())
    infile.close()
    planets = sorted(planets)
    print('\n'.join(planets[0:5]))

sortPlanets()