"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    LAB 1
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

fixedCosts = 5000
pricePerUnit = 8
costPerUnit = 6
breakEvenPoint = fixedCosts/(pricePerUnit-costPerUnit)
print(breakEvenPoint)

initialVelocity = 50
initialHeight = 5
time = 3
height = (-16)*(time**2) + initialVelocity*time + initialHeight
print(height)