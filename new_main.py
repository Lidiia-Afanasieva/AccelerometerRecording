import json
import database2
# import Gy

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D


x_base = [database2.dict_data2[item].get('x') for item in range(len(database2.dict_data2)) if database2.dict_data2[item].get("sensor") == "Accelerometer"]
y_base = [database2.dict_data2[item].get('y') for item in range(len(database2.dict_data2)) if database2.dict_data2[item].get("sensor") == "Accelerometer"]
z_base = [database2.dict_data2[item].get('z') for item in range(len(database2.dict_data2)) if database2.dict_data2[item].get("sensor") == "Accelerometer"]
time = [database2.dict_data2[item].get('time') for item in range(len(database2.dict_data2)) if database2.dict_data2[item].get("sensor") == "Accelerometer"]
first_time = int(time[0])

for item in range(len(x_base)):
    try:
        x_base[item] = float(x_base[item])
        y_base[item] = float(y_base[item])
        z_base[item] = float(z_base[item])
        time[item] = int(time[item]) - first_time
    except TypeError:
        print("TypeError", item)
print(y_base)
print(time)

plt.figure('Draw')

plt.plot(time, z_base)
plt.grid()
plt.xlabel('t, cек*10')
plt.ylabel('z, м*сек^2')
plt.show()
print(time)