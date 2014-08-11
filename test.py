import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
plt.show()

from numpy.random import normal,rand
x = normal(size=200)
plt.hist(x,bins=30)
plt.show()


key = os.urandom(32)

import platform

lib = None

if platform.system() == "Linux":
	lib = cdll.LoadLibrary( "".join([(os.getcwd()), ("/libcrypt.so")]))
else:
	lib = cdll.LoadLibrary( "".join([(os.getcwd()), ("/libcrypt.dll")]))

lib.do_crypt("test.jpg".encode("utf-8"), "test.bin".encode("utf-8"), key)
lib.do_decrypt("test.bin".encode('utf-8'), "test2.jpg".encode("utf-8"), key)
