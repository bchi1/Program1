"""This program tells the user their initials"""

#First, get the first, middle, and last name of the user
firstName = input("Please enter your first name: ")
middleName = input("Please enter your middle name: ")
lastName = input("Please enter your last name: ")

#Next, grab the intials from the first, middle, and last name
firstInitial = firstName[:1].upper()
middleInitial = middleName[:1].upper()
lastInitial = lastName[:1].upper()

#Print it out in the correct format
print("Your initials are  %s.%s.%s" % (firstInitial, middleInitial, lastInitial))