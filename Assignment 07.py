"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    ASSIGNMENT 7
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

"""
1.  Create a CSV file and name it US_Cities.csv (or US_Cities.txt) that includes the following
    information:
        
        City            State   population in 2005  population in 2015
        New York        NY      81.3                84.5
        Boston          MA      6.1                 6.4
        Seattle         WA      6.0                 6.3
        Chicago         IL      28.7                28.4
        Los Angeles     CA      37.6                39.1
        Houston         TX      21.5                23.6
        Philadelphia    PA      15.1                14.5
        San Francisco   CA      7.6                 7.5
    
    Each line of the file should have 4 fields, name of the city, state, population in 2005 (in
    100,000s), and population in 2015 (in 100,000s).

2.  Write a program that reads in the CSV file and puts cities in descending order based on the
    population of 2015. Display the top 5 cities with just the name of the city and the population
    in 2015. The program should also create a new file (name it growth.txt) with each line
    containing the name of a city and its percentage population growth from 2005 to 2015. 
"""
def main():
    cities = recordToList("US_Cities.csv")
    cities.sort(key = lambda cities:cities[3], reverse = True)
    topFiveCities(cities)
    cityGrowth(cities)

def recordToList(fileName):
    infile = open(fileName, 'r')
    listOfRecords = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(listOfRecords)):
        listOfRecords[i] = listOfRecords[i].split(',')
        listOfRecords[i][2] = eval(listOfRecords[i][2])
        listOfRecords[i][3] = eval(listOfRecords[i][3])
    return listOfRecords

def topFiveCities(listName):
    print("{0:20}{1:9}{2:22}{3:18}".format("name of the city", "state", "population in 2005", "population in 2015"))
    print()
    for i in range(5):
        print("{0:20}{1:9}{2:18}{3:22}".format(listName[i][0], listName[i][1], listName[i][2], listName[i][3]))

def cityGrowth(listName):
    outfile = open("growth.txt", 'w')
    for element in listName:
        growth = (element[3]-element[2])/element[2]
        outfile.write(element[0] + ',' + "{:.2%}".format(growth) + "\n")

main()
