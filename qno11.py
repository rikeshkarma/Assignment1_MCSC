#Write a program to find the smallest integer n such that 3^n ≥ 2000

n=0
a=3**n
while a<=2000:
    n=n+1
    a=3**n
print(n)
