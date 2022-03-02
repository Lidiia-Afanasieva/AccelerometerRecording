import json
import database
import database2

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

x_base = [database2.dict_data2[item].get('x') for item in range(len(database2.dict_data2))]
print(float(x_base[0]))
y_base = [database2.dict_data2[item].get('y') for item in range(len(database2.dict_data2))]
z_base = [database2.dict_data2[item].get('z') for item in range(len(database2.dict_data2))]


x_base.pop(1454)
y_base.pop(1454)
z_base.pop(1454)

for item in range(len(x_base)):
    try:
        x_base[item] = float(x_base[item])
        y_base[item] = float(y_base[item])
        z_base[item] = float(z_base[item])
    except TypeError:
        print("TypeError", item)
print(x_base)
print(y_base)
print(z_base)

fig = plt.figure()
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

X = [0, 1.1, 1.8, 3.1, 4.0]
Y = [2, 2.4, 4.3, 3.5, 2.5]
# X, Y = np.meshgrid(X, Y)
Z = [2, 2.4, 4.3, 3.5, 2.5]
#ax = fig.add_subplot(111, projection='3d')
ax.plot(x_base, y_base, z_base)
plt.show()
