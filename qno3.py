#Create an array of 9 evenly spaced numbers going from 0 to 29 (inclusive) and give it the variable name 𝑟.
#Find the square of each element of the array (as simply as possible).
#Find twice the value of each element of the array in two different ways: (i) using addition and
# (ii) using multiplication.


from numpy import*
r=linspace(0,29,9)
print("The 9 evenly spaced numbers going from 0 to 29 are: ")
for i in r:
    print(i)

a=r**2
print("The square of each element of the array are: ")
for i in a:
    print(i)

print("The twice value of each element in the array using addition: ")
for i in r:
    print(i+i)

print("The twice value of each element in the array using multiplication: ")
for i in r:
    print(2*i)
