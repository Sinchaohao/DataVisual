# @Author:sch
# @Time:2022/07/20
# @File:highs_lows.py
# @software: PyCharm

import csv

import matplotlib.pyplot as plt

filename = 'sitka_weather_07-2014.csv'

# 从文件中获取最高气温
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     # enumerate() 来获取每个元素的索引及其值
    #     print(index, column_header)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

# 设置图形的格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major',labelsize=16)

plt.show()
