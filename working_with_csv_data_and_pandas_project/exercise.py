# with open('weather_data.csv', 'r') as file:
#     lines = file.readlines()
#
# data = []
#
# for line in lines[1:]:
#     data_line = line.strip().split(',')
#
#     data.extend(data_line)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#
#     # extracting all temperatures as integers
#     temperatures = [int(row[1]) for row in data if row[1] != 'temp']
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()

avg_temp = sum(temp_list) / len(temp_list)
print(f"{avg_temp:.1f}")

# getting max temp using pandas method
max_temp = data["temp"].max()
print(max_temp)

# get data in columns
print(data["condition"])
print(data.condition)

# get data in a row
print(data[data.day == "Monday"])

# print row with max temp
print(data[data.temp == data.temp.max()])

# converting celsius to fahrenheit
data.temp = data.temp * 9/5 + 32

print(data)