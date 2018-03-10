from random import randint
import numpy as np
from math import *
import matplotlib.pyplot as plt

x1 = np.array([2*pi*(i/100.0) for i in range(0, 50)])
x2 = np.array([2*pi*(i/100.0) for i in range(-50, 50)])
y1 = np.sin(x1)
y2 = np.sin(x2)

back = [i for i in range(-25, 0)]
a = [i/5.0 for i in range(0, 50)]
b = [(i/10.0)+10 for i in range(0, 100)]
c = [(i/5.0)+20 for i in range(0, 50)]
front = [i for i in range(30, 55)]
val = [0 for i in range(25)]

# Half positive
plt.plot(a, 2*y1)

# Half negative
plt.plot(c, -2*y1)

# Full
plt.plot(b, 20*y2)
plt.plot(back, val)
plt.plot(front, val)
plt.show()
