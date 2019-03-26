"""
AUTHOR:     ERYL KENN VICTORINO
PURPOSE:    ASSIGNMENT 8
            from "Open Source Programming in Python" Course
            with Professor Ivy Liu
MOD DATE:   3/24/2019
"""

"""
1.  The text file Exchrate.txt that has the information about the currencies of 49 major countries
    will be given. The first few lines of the file are as follows:
        America,Dollar,1
        Argentina,Peso,8.405692
        Australia,Dollar,1.070835
        Austria,Euro,0.760488
    Each line of the file gives the name of a country, the name of its currency, and the number of
    units of the currency that were equal to one American dollar (called the exchange rate). For
    instance, one American dollar is equal to 8.405692 Argentina pesos.
    Write a program that requests the names of two countries and an amount of money. The
    program then converts the amount from the first country’s currency to the equivalent amount
    in the second country’s currency.
    If user entered America as the first country, Brazil as the second country, and amount of 100,
    Your final print message should read as:
        100 dollars from America equals 840.5692 pesos from Argentina
"""
# just your old fashion main function
def main():
    runProgram()

# this creates a dictionary that matches the country to a currency and an exchange rate
def createDictionary():
    infile = open("Exchrate.txt")
    fileInfo = list(infile)
    curDict = {}
    for line in fileInfo:
        lineInfo = line.lower().split(",")
        curDict[lineInfo[0]] = (lineInfo[1], float(lineInfo[2].replace("\n", "")))
    infile.close()
    return curDict

# this collects user input
def getInput(dictName):

    # this splits up the list of countries to display more per row for the user to choose from
    print("Here is a list of countries to choose from:")
    countryList = list(sorted(dictName.keys()))
    mod = len(countryList)%3
    index = int(len(countryList) - mod)
    for i in range(int(index/3)):
        print("{0:20}{1:20}{2:20}".format(countryList[i], countryList[i + int(index/3) + 1], countryList[i + int(2*index/3) + 1]).title())
    if mod == 2:
        print("{0:20}{1:20}".format(countryList[int(index/3)], countryList[int(2*index/3) + 1]).title())
    elif mod == 1:
        print("{0:20}".format(countryList[int(index/3)].title()))
    print()

    # this takes the user input for what we need and keeps asking until they provide the proper information
    origCountry = input("Please choose your currency's country of origin from the list above: ") 
    while origCountry.lower() not in countryList:
        origCountry = input("You must choose from the list above!: ")
    newCountry = input("Please choose the country of the currency you wish to convert to from the list above: ")
    while newCountry.lower() not in countryList:
        newCountry = input("You must choose from the list above!: ")
    amount = ''
    while type(amount) != float:
        try:
            amount = float(input("Please enter the amount of your current currency: ").replace(',', ''))
            # I like to add the replace function in case the user writes a dollar sign or commas in their value
            
        except ValueError:
            print("The amount must be a number!")
            amount = ''
    return (origCountry.lower(), newCountry.lower(), amount)

# this is the function that does the actual converting of the currency using the information we collected
def currencyConverter(origCountry, newCountry, amount, curDict):
    newAmount = (amount/curDict[origCountry][1])*curDict[newCountry][1]
    return newAmount

# this wasn't part of the homework but I added it to make my code a little more grammatically correct by pluralizing properly
def pluralizeCurrency(country, currency, amount):
    check = ('2', '3', '4')

    # these currencies do not have a plural form and stay in their singular form
    if currency in ["baht", "forint", "rand", "won", "yen", "yuan"]:
        pluralCurrency = currency

    # these currencies have a plural form with a different spelling than usual
    elif currency == "real":
        pluralCurrency = "reais"
    elif currency == "koruna":
        pluralCurrency = "korun"
    elif currency == "krone":
        pluralCurrency = "kroner"
    elif currency == "krona":
        if country == "Sweden":
            pluralCurrency = "kronor"
        elif country == "Iceland":
            pluralCurrency = "kronur"
    elif currency == "sheqel":
        pluralCurrency = "sheqalim"
    elif currency == "sol":
        pluralCurrency = "soles"
    elif currency == "leu":
        pluralCurrency = "lei"
    elif currency == "ruble":
        pluralCurrency = "rubli"

    # these currencies have different plural forms depending on what number the amount ends with
    elif currency == "zloty":
        if type(amount) == int and str(amount).endswith(check):
            pluralCurrency = "zlote"
        else:
            pluralCurrency = "zlotych" 
    elif currency == "hryvnia":
        if type(amount) == int and str(amount).endswith(check):
            pluralCurrency = "hryvni"
        else:
            pluralCurrency = "hryven"

    # the rest of the plural currencies just end with an s
    else:
        pluralCurrency = currency + "s"
    return pluralCurrency

# this displays our results and does some last minute editing for grammatical purposes
def displayOutput(origCountry, newCountry, amount, curDict, newAmount):

    # this turns numbers that end with ".0" to an integer
    if str(amount).endswith(".0"):
        amount = int(amount)
    if str(amount).endswith(".0"):
        newAmount = int(newAmount)

    # this pluralizes the currency by default
    origCurrency = pluralizeCurrency(origCountry, curDict[origCountry][0], amount)
    newCurrency = pluralizeCurrency(newCountry, curDict[newCountry][0], newAmount)

    # this reverts the currency back to its singular for if the corresponding amount is 1
    if amount == 1:
        origCurrency = curDict[origCountry][0]
    if newAmount == 1:
        newCurrency = curDict[newCountry][0] 

    # some countries technically start with the word "the" so I implemented that
    startsWithThe = ["Czech Rep.", "European Union", "Netherlands", "Philippines", "U.A.E.", "Ukraine", "United Kingdom"]
    if origCountry in startsWithThe:
        origCountry = "The " + origCountry
    if newCountry in startsWithThe:
        newCountry = "The " + newCountry

    # once everything is edited and all set, this prints the output
    print("{:,.2f}".format(amount), origCurrency, "from", origCountry.title(), "equals", "{:,.2f}".format(newAmount), newCurrency, "from", newCountry.title())

# I added this to give the user the option to keep using the program
def runProgram():
        
    # this is a basic creeting and introduction
    print("Hello, welcome to Kenn's Cool Currency Converter!")
    print()

    curDict = createDictionary()

    # this will this will loop until the user agrees to keep using the program or close it
    origCountry, newCountry, amount = getInput(curDict)
    newAmount = currencyConverter(origCountry, newCountry, amount, curDict)
    displayOutput(origCountry, newCountry, amount, curDict, newAmount)
    loop = input("Try again?(type 'yes' to try another conversion): ").lower()
    if loop == ("yes"):
        runProgram()
                     
main()
