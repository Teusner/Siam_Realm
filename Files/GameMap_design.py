import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

size = 64*5+6*5
print(size)
gridColor = [45/255, 52/255, 54/255]
mapColor = [254/255, 202/255, 87/255]

G = np.zeros((size, size, 3))

for i in range(size):
    for j in range(size):
        G[i, j] = mapColor

for k in range(0,6):
    G[69*k: 69*k+5, :] = gridColor
    G[:, 69*k:69*k+5] = gridColor

plt.imshow(G)
plt.box(on=None)
plt.xticks([])
plt.yticks([])
plt.axes().set_aspect('equal')
plt.axis([0, size, 0, size])
plt.show()
mpimg.imsave('gamemap.png', G)
