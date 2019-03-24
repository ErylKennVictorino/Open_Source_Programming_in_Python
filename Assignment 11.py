"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    ASSIGNMENT 11
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

"""
1.  Write a program to create the line chart using the data in the following table:
    
        Freshman life goals (% of students committed to goal)
                                                    1978    1988    1998    2008
        Be very well off financially                59      74      73      77
        Develop a meaningful philosophy of life     60      43      44      51
        
    Make sure to include the title of the graphs, label all data clearly, and indicate which line
    represent which category.
"""
import turtle

# data sets. I put them in tuples since they don't need to be changed
y1 = (59, 74, 73, 77)
y2 = (60, 43, 44, 51)
x = (1978, 1988, 1998, 2008)

# just your average main function calling all the other functions
def main():
    t = turtle.Turtle()
    t.hideturtle()
    printTitle(t)
    drawLine(t, -250, -150, 250, -150, "black")
    drawLine(t, -250, -150, -250, 250, "black")
    drawTickMarks(t, x, y1, y2)
    labelXAxis(t)
    graphPoints(t, x, y1, "red", "right")   # I wanted to make the aligntment different for these
    graphPoints(t, x, y2, "blue", "left")   # because the first elements overlapped
    makeLegend(t)

# clearly prints the title
def printTitle(t):
    t.up()
    t.goto(0, 300)
    t.write("Freshman life goals (% of students committed to goal)", align = "center", font=("Arial", 24, "bold"))

# this is my line drawer
def drawLine(t, x1, y1, x2, y2, colorP):
    t.up()
    t.goto(x1, y1)
    t.down()
    t.pencolor(colorP)
    t.goto(x2, y2)

# this is my dot drawer, I separated it from drawLine so that I can write the values next to it
def drawDot(t, x, y, diameter, colorP):
    t.up()
    t.pencolor(colorP)
    t.goto(x, y)
    t.dot(diameter)

# labels the x-axis (I tried to do the same with the y-axis but I couldnt figure out how to rotate text)
def labelXAxis(t):
    t.up()
    t.goto(0, -200)
    t.write("Year", align = "center", font=("Arial", 12, "normal"))

# draws the tick marks and their values
def drawTickMarks(t, x, y1, y2):
    for i in range(1, len(x)+1):
        drawLine(t, -250 + 100*i, -150, -250 + 100*i, -140, "black")
        t.up()
        t.goto(-250 + 100*i, -170)
        t.write(str(1968+ 10*i), align = "center")
    for i in range(1, (max(y1+y2)//10 + 1)):
        drawLine(t, -250, -150 + 50*i, -240, -150 + 50*i, "black")
        t.up()
        t.goto(-270, -150 + 50*i)
        t.write(str(10*i), align = "center")

# plots the points and connects the dots
def graphPoints(t, x, y, colorP, align):
    for i in range(len(x)):
        drawDot(t, 10*x[i]-19930, 5*y[i]-150, 5, colorP)
        t.up()
        t.goto(10*x[i]-19930, 5*y[i]-150)
        t.write(str(y[i]), align = align) 
    for i in range(len(x)-1):
        drawLine(t, 10*x[i]-19930, 5*y[i]-150, 10*x[i+1]-19930, 5*y[i+1]-150, colorP)

# this is my legend for the graph
def makeLegend(t):
    t.up()
    t.pencolor("black")
    t.goto(0, -100)
    t.down()
    t.goto(250, -100)
    t.goto(250, -25)
    t.goto(0, -25)
    t.goto(0, -100)
    t.up()
    t.goto(50, -55)
    t.write("Be very well off financially", align = "left", font=("Arial", 8, "normal"))
    t.up()
    t.goto(50, -80)
    t.write("Develop a meaningful philosophy of life", align = "left", font=("Arial", 8, "normal"))
    drawDot(t, 25, -50, 20, "red")
    drawDot(t, 25, -75, 20, "blue")
    
main()