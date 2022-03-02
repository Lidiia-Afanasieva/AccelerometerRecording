import json
import database
import database2

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D




# accelerometer_data = open(t'data.json')

# with open(accelerometer_data, 'r') as work_data:  # по умолчанию открывает на чтение

# objects = ijson.items(accelerometer_data, 'columns.item')  # по ключу вытащить
# columns = list(objects)
# print(columns)
# print(accelerometer_data.read())
# {"sensor":"Orientation","time":"1645608253593260500",
# "seconds_elapsed":"14.255260498046875","qz":"-0.6444154977798462",
# "qy":"-0.16099749505519867","qx":"0.21591924130916595",
# "qw":"0.7156726717948914","roll":"0.05590078979730606",
# "pitch":"-0.5428210496902466","yaw":"1.4816685914993286"}
# адо обрезать файл и разделить на столбцы, глянуть в нампае

# x_base = [item for item in accelerometer_data]
# for i in range(len(list(accelerometer_data.read()))):
#     x_base.append(accelerometer_data[i][5])
# print(accelerometer_data)
# print(x_base)
# with open('data.json', "r") as f:
#     part = [ i.strip().split('},{') for i in f.readlines()]
#     print(part[1])
#print([database.dict_data[item].get('x') for item in range(len(database.dict_data))])
x_base = [database2.dict_data2[item].get('x') for item in range(len(database2.dict_data2))]
print(float(x_base[0]))
y_base = [database2.dict_data2[item].get('y') for item in range(len(database2.dict_data2))]
z_base = [database2.dict_data2[item].get('z') for item in range(len(database2.dict_data2))]
# try:
#     x_base = [float(item) for item in x_base]
#     print(x_base)
# except TypeError:
#     print("TypeError")

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
#
# # print(y_base)
# print(len(x_base))
# print(x_base)
# # print(len(y_base))
# print(len(z_base))

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
