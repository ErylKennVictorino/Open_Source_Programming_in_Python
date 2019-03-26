"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    ASSIGNMENT 1
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

"""
1.  The American College of Sports Medicine recommends that you maintain your training
    heart rate during an aerobic workout. It is computed as 0.7 * (220 – a) + 0.3 * r, where a is
    your age and r is your resting heart rate (your pulse when you first awaken). Write a program
    to request a person’s age and resting heart rate and display their training heart rate.
"""
def tHR():
    age = input("Enter your age: ")
    rHR = input("Enter your resting heart rate: ")
    #this checks if the inputs are integers
    try:
        a = int(age)
        r = int(rHR)
        trHR = 0.7*(220 - a) + 0.3*r
        print("Training heart rate: " + str(trHR) + " beats/min")
    #this prompts a error message if the user doens't input a integer
    except ValueError:
        print("The age or resting heart rate must be an integer.")
        tHR()

tHR()

"""
2.  The cost of the electricity used by a device is given by the formula:
    cost of electricity (in dollars) = (wattage of device * hours used)/(1000 * cost per kWh (in cents))
    Where kWh is an abbreviation for “kilowatt hour”. The cost per kWh of electricity varies
    with locality. Suppose the current average cost of electricity for a residential customer in the
    United States is 11.76 cents per kWh. Write a program that allows the user to calculate the
    cost of operating an electrical device.
"""
def electricityCost():
    watt = input("Enter wattage: ")
    hours = input("Enter numer of hours used: ")
    price = input("Enter price per kWh in cents: ")
    try:
        w = float(watt)
        h = float(hours)
        p = float(price)
        cost = (w*h)/(1000*p)
        print("Cost of electricity: $" + str(round(cost, 2)))
    except ValueError:
        print("The wattage, hours used, or price per kWh is invalid.")
        electricityCost()

electricityCost()
