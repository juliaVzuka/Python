# -*- coding: utf-8 -*-
"""2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1akriL9FFwdXbmX5e0wgEdJCINkmYd3IG

1.2
"""

n = int(input(f"Введите размерность вектора: "))
a = 0
length = 0
for i in range(n):
  a = int(input(f"Введите {i+1}-ю координату вектора: "))
  length += a ** 2
print(f"Длина вектора равна: {length}")

"""3.1 Окружность"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import math
x1 = []
x2 = []
y1 = []
y2 = []
r = 5
for i in range(r * 1000 +1):
  x_ = i / 1000
  x1.append(x_)
  x2.append(-x_)
  y1.append(math.sqrt(r ** 2 - x_ ** 2))
  y2.append(-math.sqrt(r ** 2 - x_ **  2))
ax = plt.axes()
ax.set_aspect(1)
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x2, y2)
plt.plot(x2, y1)
plt.xlabel("x")
plt.ylabel("y")



"""3.2 Эллипс"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import math
x1 = []
x2 = []
y1 = []
y2 = []
a = 5
b = 3
for i in range(a * 1000 +1):
  x_ = i / 1000
  x1.append(x_)
  x2.append(-x_)
  y1.append(b * math.sqrt(1 - x_ ** 2 / a ** 2))
  y2.append(- b * math.sqrt(1 - x_ ** 2 / a** 2))
fig = plt.figure()
ax = plt.axes()
ax.set_aspect(1)
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x2, y2)
plt.plot(x2, y1)
plt.xlabel("x")
plt.ylabel("y")

"""3.3 Гипербола"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import math
x1 = []
x2 = []
y1 = []
y2 = []
a = 1
b = 2
for i in range(a * 1000 +1):
  x_ = i / 1000
  x1.append(x_)
  x2.append(-x_)
  y1.append(b * math.sqrt(1 + x_ ** 2 / a ** 2))
  y2.append(- b * math.sqrt(1 + x_ ** 2 / a** 2))
fig = plt.figure()
ax = plt.axes()
ax.set_aspect(1)
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x2, y2)
plt.plot(x2, y1)
plt.xlabel("x")
plt.ylabel("y")

"""5.1"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
x = np.arange(-50, 50, 1)
y = np.arange(-50, 50, 1)
x, y = np.meshgrid(x, y)
z1 = 2 * x + 5 * y
ax.plot_surface(x, y, z1)
z2 = 2 * x + 5 * y + 500
ax.plot_surface(x, y, z2)
show()

"""5.2"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
x = np.arange(-50, 50, 1)
y = np.arange(-50, 50, 1)
x, y = np.meshgrid(x, y)
z1 = x ** 2 - y **2
z2 = x ** 2 + y ** 2
ax.plot_surface(x, y, z1)
ax.plot_surface(x, y, z2)
show()
