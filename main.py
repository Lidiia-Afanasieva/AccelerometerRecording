import ijson

accelerometer_data = open(r'data.json')

# with open(accelerometer_data, 'r') as work_data:  # по умолчанию открывает на чтение

# objects = ijson.items(accelerometer_data, 'columns.item')  # по ключу вытащить
# columns = list(objects)
# print(columns)
print(accelerometer_data.read())
# {"sensor":"Orientation","time":"1645608253593260500",
# "seconds_elapsed":"14.255260498046875","qz":"-0.6444154977798462",
# "qy":"-0.16099749505519867","qx":"0.21591924130916595",
# "qw":"0.7156726717948914","roll":"0.05590078979730606",
# "pitch":"-0.5428210496902466","yaw":"1.4816685914993286"}
# адо обрезать файл и разделить на столбцы, глянуть в нампае