# @Author:sch
# @Time:2022/07/20
# @File:highs_lows.py
# @software: PyCharm

import csv

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
        highs.append(row[1])

    print(highs)
