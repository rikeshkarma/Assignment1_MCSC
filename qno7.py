from math import*
print("Equation in the form of ax2+bx+c: ")
a=float(input("Enter the value of a: "))
while a==0:
    a=float(input("The value of a cannot be 0, Please enter the value again: "))

b=float(input('Enter the value of b: '))
c=float(input("Enter the value of c: "))

dis=b*b-4*a*c
w=sqrt(dis)
root1=((-b+w)/(2*a))
root2=((-b-w)/(2*a))

if dis==0:
    print("The nature of roots is real and equal. ")
    print("The two roots of the equation are: " + str(root1) + " and " + str(root2))
elif dis<0:
    print("Roots are unreal. ")
    print("No roots and discriminant is less than 0")
else:
    print("Roots are real and unequal. ")
    print("The two roots of the equation are: " + str(root1) + " and " + str(root2))
