import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100)
y = x*2
z = x*x

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')
plt.show()

fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.2,0.2])
plt.show()

fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.2,0.2])
ax1.plot(x,y)
ax2.plot(x,y)
plt.show()

fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax1.set_xlim([0,100])
ax1.set_ylim([0,10000])
ax2 = fig.add_axes([0.2,0.5,0.2,0.2])
ax2.set_ylim([30,50])
ax2.set_xlim([20,22])
ax1.plot(x,z)
ax2.plot(x,y)
plt.show()

fig, ax = plt.subplots(nrows=1, ncols=2)
plt.show()

fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].plot(x, y, 'b--', lw=3)
ax[1].plot(x, z, 'r', lw=3)
plt.show()

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12,2))
ax[0].plot(x, y, 'b--', lw=3)
ax[1].plot(x, z, 'r', lw=3)
plt.show()
