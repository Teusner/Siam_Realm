import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

G = np.zeros((530, 530, 3))

for i in range(530):
    for j in range(530):
        for k in range(3):
            G[i, j, k] = 1

for k in range(0,6):
    G[105*k: 105*k+5, :, 0] = 0.6
    G[105*k: 105*k+5,:, 1] = 0.6
    G[105*k: 105*k+5,:, 2] = 0.6

    G[:, 105*k:105*k+5, 0] = 0.6
    G[:, 105*k:105*k+5, 1] = 0.6
    G[:, 105*k:105*k+5, 2] = 0.6

plt.imshow(G)
plt.box(on=None)
plt.xticks([])
plt.yticks([])
plt.axes().set_aspect('equal')
plt.axis([0, 530, 0, 530])
plt.show()
mpimg.imsave('gamemap.png', G)
