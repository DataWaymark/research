import matplotlib
from matplotlib import pyplot as plt, patches
from random import random

plt.rcParams["figure.figsize"] = [15.00, 15.00]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()

ax = fig.add_subplot(111)

rect = patches.Rectangle((2, 2), 8, 8, fill=None, color='black')

circle = patches.Circle((6, 6), radius=4, fill=None, color='black')

ax.add_patch(rect)
ax.add_patch(circle)

plt.xlim([-10, 10])
plt.ylim([-10, 10])

plt.axis('equal')

minVal = 2
maxVal = 10
count = 1000

ptsX = [0 for i in range(count)]
ptsY = [0 for i in range(count)]

for i in range(count):
	ptsX[i] = minVal + random()*(maxVal - minVal)
	ptsY[i] = minVal + random()*(maxVal - minVal)
	plt.plot(ptsX[i], ptsY[i], marker="o", markersize=2, markeredgecolor="red", markerfacecolor="green")


plt.show()

