"""given the amount of money requested
tells the minimum number of bill required to meet the amount"""

#first, get the amount of money from the user
moneyRemaining = int(input("Please enter the amount of money you wish to withdraw: "))

#next get the number of 100 dollar bills
num100 = moneyRemaining // 100
moneyRemaining = moneyRemaining % 100
print("You received %d hundred(s)" % num100)

#next get the number of 50 dollar bills
num50 = moneyRemaining // 50
moneyRemaining = moneyRemaining % 50
print("You received %d fifty(s)" % num50)

#next get the number of 20 dollar bills
num20 = moneyRemaining // 20
moneyRemaining = moneyRemaining % 20
print("You received %d twenty(s)" % num20)

#next get the number of 10 dollar bills
num10 = moneyRemaining // 10
moneyRemaining = moneyRemaining % 10
print("You received %d ten(s)" % num10)

#next get the number of 5 dollar bills
num5 = moneyRemaining // 5
moneyRemaining = moneyRemaining % 5
print("You received %d five(s)" % num5)

#next get the number of 1 dollar bills
num1 = moneyRemaining // 1
moneyRemaining = moneyRemaining % 1
print("You received %d one(s)" % num1)
