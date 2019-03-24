"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    LAB 4
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

"""
1.  Copy the file “using main.py” from Piazza. Modify the main() function in the file to have a
    separate function, namely getInput, that will get user input on principal of a mortgage, annual
    interest rate, and number of years to pay off. Make the necessary computation and then return
    the principal, monthly interest rate, and number of payments for the mortgage. The code is
    largely ready for you there. You only need to wrap the code into a function and return values
    that are ready for passing into the function mnth_pay.
"""
def main():
    print("Calculate monthly mortgage payment!")
    print()

    P, r_annual, r, n, n_yrs = getInput()

    ## calling the mortgage function
    monthlyPlay = mnth_pay(P, r, n)

    ## calling the output function
    output_Data(P, r_annual, monthlyPlay, n_yrs)

def getInput():
    P = float(input("Enter the principal of your mortgage: "))
    while not (P > 0):
        print("The principal must be greater than 0!")
        P = float(input("Enter the principal of your mortgage: "))
    r_annual = float(input("Enter the annual interest rate,  i.e., 4.25 for 4.25 percent: "))
    while not (100 > r_annual > 0):
        print("The annual interest rate must be strictly between 0 and 100!")
        r_annual = float(input("Enter the annual interest rate, i.e., 4.25 for 4.25 percent: "))
    n_yrs = float(input("Enter the duration of your mortgage in years: "))
    while not (n_yrs > 0):
        print("The mortgage duration must be greater than 0!")
        n_yrs = float(input("Enter the duration of your mortgage in years: "))
    r = (r_annual / 12) / 100
    n = (n_yrs * 12)
    return (P, r_annual, r, n, n_yrs)


def mnth_pay(P, r, n):
    """
    Input:  P, the principal
            r, monthly interest rate
            n, duration of loan in months
    Returns monthly mortgage payment
    """
    M = P * ((r * (1 + r)**n) / ((1 + r)**n - 1))
    return M

def output_Data(P,r_annual, pay, n_yrs):
    """
    Input:  P, the principal
            r_annual, annual interest rate
            pay, the monthly payment after calculation
            n_yrs, duration of loan in years
    """
    print()
    print("With a principal of ${0:,.2f}; an annual interest rate of {1:g}%;".format(P, r_annual)) 
    print("and a duration of {:g} years: Your monthly payment is about: ${:,.2f}".format(n_yrs, pay))
    
main()