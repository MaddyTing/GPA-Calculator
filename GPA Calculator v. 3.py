
def GPAcalc(w, x):
    if (w == "A" or w == "a"):
        if(x == 1):
            return(5)
        elif(x == 0):
            return(4)
    elif (w == "B" or w == "b"):
        if(x == 1):
            return(4)
        elif(x == 0):
            return(3)
    elif (w == "C" or w == "c"):
        if(x == 1):
            return(3)
        elif(x == 0):
            return(2)
    elif (w == "D" or w == "d"):
        if(x == 1):
            return(2)
        elif(x == 0):
            return(1)
    elif (w == "F" or w == "f"):
        if(x == 1):
            return(1)
        elif(x == 0):
            return(0)

def averageGPA(y, z):
    return y / z
    
classes = int(input("How many Classes are you taking? "))
sumGPA = 0

for i in range(classes):
    grade = input("\nEnter your Letter Grade: ")
    weight = int(input("Is it weighted? (1 = yes, 0 = no) "))
    if(GPAcalc(grade, weight) == None):
        print("Your GPA score is: Invalid")
    else:
        print("Your GPA score is: " + str(GPAcalc(grade, weight)))
    sumGPA = sumGPA + GPAcalc(grade, weight)

print("\nYour weighted GPA is a " + str(float(averageGPA(sumGPA, classes))) + ".")

