#The position of a ball at time 𝑡 dropped with zero initial velocity from a height ℎ0 is given by 𝑦 = ℎ0 − 0.5𝑔𝑡2
#where 𝑔 = 9.8 𝑚/𝑠2. Suppose ℎ0 = 10 𝑚. Find the sequence of times when the ball passes each half meter assuming
#the ball is dropped at 𝑡 = 0. Hint: Create a NumPy array for y that goes from 10 to 0 in increments of -0.5 using
#the arrange function. Solving the above equation for t, show that 𝑡 = 2 ℎ0−𝑦 𝑔 .


from numpy import*

g=9.8
h0=10
y=numpy.arange(10,0,-0.5)
t=numpy.sqrt(2(h0-y))/g
