import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [6, 5]
plt.rcParams["figure.autolayout"] = True

x = np.linspace(-2, 2, 1000)
y1 = np.sqrt(1 - (abs(x) - 1) ** 2)
y2 = -3 * np.sqrt(1 - (abs(x) / 2) ** 0.5)

plt.fill_between(x, y1, color='purple')
plt.fill_between(x, y2, color='purple')

plt.title("My heart")
plt.text(0, -1.0, 'you', fontsize=24, color='white',
horizontalalignment='center')

plt.show()