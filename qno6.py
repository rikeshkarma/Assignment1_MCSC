#Plot the functions 𝑦 = 𝑠𝑖𝑛 𝑥 and 𝑦 = 𝑐𝑜𝑠 𝑥 for  −2𝜋 ≤ 𝑥 ≤ 2𝜋 on the same plot.
#Plot 𝑦 = 𝑠𝑖𝑛 𝑥 in the color red and 𝑦 = 𝑐𝑜𝑠 𝑥 in the color blue and include a legend to label the two curves.
#Place the legend within the plot, but such that it does not cover either of the sine or cosine traces.

import matplotlib.pyplot as plt
import numpy as np
from math import*

plt.xlabel('-360<x<360')
plt.ylabel('-1<x<1')
plt.title("Sin & Cos")
x=np.arange(-360,360)
plt.plot(x,np.sin(x*(np.pi/180)),'r',label="sin")
plt.plot(x,np.cos(x*(np.pi/180)),'b',label="cos")
plt.legend()
plt.show()
