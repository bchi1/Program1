"""this program figures out what grade you need to get on the
final to get the desired grade in the class"""

#first get the grade the user wants in the class
#then the percent needed for the grade
#then the current percent in the class
#then the weight of the final
gradeWanted = input("Enter the grade you want in the class: ")
percentForGrade = float(input("Enter the percent you need to get that grade: "))
currentPercent = float(input("Enter your current percent in the class: "))
weightFinal = float(input("Enter the weight of the final: ")) / 100

#calculate the weight to give to the current percentage
weightRemaining = 1 - weightFinal

#calculates the grade needed on the final to get the grade you want
finalGrade = (percentForGrade - (weightRemaining * currentPercent)) / weightFinal

#prints the final grade needed in the correct format
print("You need to get at least %.2f%% on the final to get a " % finalGrade + gradeWanted + " in the class.")