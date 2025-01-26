#asks user for numeric grade
nGrade = float(input("Enter numeric grade here (i.e 90): "))

#returns letter grade based on numeric grade input using range of letter grade
if nGrade >= 90:
    print("The letter grade is A+")
elif nGrade >= 80 and nGrade <90:
    print("The letter grade is A")
elif nGrade >= 70 and nGrade <80:
    print("The letter grade is B")
elif nGrade >= 60 and nGrade <70:
    print("The letter grade is C")
elif nGrade >= 50 and nGrade <60:
    print("The letter grade is D")
else:
    print("The letter grade is F")