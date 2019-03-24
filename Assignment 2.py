"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    ASSIGNMENT 2
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

"""
1.  An investor’s stock portfolio consists of four Exchange Traded Funds (SPY,
    QQQ, EEM, and VXX). Write a program that requests the amount invested in each fund as input.
    Then display the total amount invested and each fund’s percentage of the total amount invested.
"""
def totalInvestment():
    try:
        spy = input("Enter amount invested in SPY: ")
        qqq = input("Enter amount invested in QQQ: ")
        eem = input("Enter amount invested in EEM: ")
        vxx = input("Enter amount invested in VXX: ")
        s = float(spy)
        q = float(qqq)
        e = float(eem)
        v = float(vxx)
        t = s + q + e + v
        sp = s/t
        qp = q/t
        ep = e/t
        vp = v/t
        print()
        print("{0:6s}{1:>12s}".format("ETF", "PERCENTAGE"))
        print("-" * 18)
        print("{0:6s}{1:10.2%}".format("SPY", sp))
        print("{0:6s}{1:10.2%}".format("QQQ", qp))
        print("{0:6s}{1:10.2%}".format("EEM", ep))
        print("{0:6s}{1:10.2%}".format("VXX", vp))
        print()
        print("TOTAL AMOUNT INVESTED: " + '${:,.2f}'.format(t))
    except ValueError:
        print("The input must be a number.")
        totalInvestment()

totalInvestment()