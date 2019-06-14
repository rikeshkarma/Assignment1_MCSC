#Plot the function 𝑦 = 3𝑥2  for −3 ≤ 𝑥 ≤ 3. Include enough points (say 100 points)
#so that the curve you plot appears smooth. Label the axes x and y.

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,100)
y=3*x**2
plt.plot(x,y)
plt.title("y=3x2")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
