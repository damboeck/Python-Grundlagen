
# install plotlib  with:
# pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6,3])
ypoints = np.array([0, 250,3])

plt.plot(xpoints, ypoints)
plt.show()
