g=9.8
h=1.2
v=5.4

time=input('Enter a time in sec ?\n')
t=float(time)

height=h+(v*t)-(0.5*g*t*t)

print("The required height is " + str(height))

v2=v-(g*t)

print('The velocity after t sec is '+ str(v2))
