#Unweighted

def GPAcalc(w):
    if (w == "A" or w == "a"):
        return (4)
    elif (w == "B" or w == "b"):
        return (3)
    elif (w == "C" or w == "c"):
        return (2)
    elif (w == "D" or w == "d"):
        return (1)
    elif (w == "F"or w == "f"):
        return (0)

#MAIN
grade = input("Enter your Letter Grade: ")

if(GPAcalc(grade) == None):
    print("Your GPA score is: Invalid")
else:
    print("Your GPA score is: " + str(GPAcalc(grade)))

