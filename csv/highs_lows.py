import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 获取最高温度
    highs = []
    dates = []
    lows = []
    for row in reader:
        try:
            low = int(row[9])
            high = int(row[8])
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
        # 遇到‘’，即没有温度的情况下，设置为-1, 打印错误
        except ValueError:
            print(current_date, 'missing date')
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)

    print(highs)
    print(dates)
    print(lows)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

# 设置图像的格式
plt.title("Daily high temperatures", fontsize=24)
plt.xlabel('', fontsize=16)
# 绘制斜的日期
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()