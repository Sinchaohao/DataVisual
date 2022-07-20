# @Author:sch
# @Time:2022/07/20
# @File:highs_lows.py
# @software: PyCharm

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# filename = 'sitka_weather_07-2014.csv'
filename = 'sitka_weather_2014.csv'
# 从文件中获取日期与最高气温
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     # enumerate() 来获取每个元素的索引及其值
    #     print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)

    print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
# alpha 指定颜色的透明度。Alpha 值为0表示完全透明，1（默认设置）表示完全不透明
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)

# 设置图形的格式
plt.title("Daily high temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major',labelsize=16)

plt.show()
