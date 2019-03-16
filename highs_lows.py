import csv
from datetime import datetime

from matplotlib import pyplot as plt

#从文件中获取日期和最高气温和最低气温
filename = 'F:\date\分析天气\death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    

    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_time = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_time, 'missing date')
        else:
            highs.append(high)
            dates.append(current_time)        
            lows.append(low)

    #根据数据绘制图形
    fig = plt.figure(dpi=128,figsize=(10,6)) 
    plt.plot(dates,highs,c='red')
    plt.plot(dates,lows,c='blue')
    plt.fill_between(dates,highs,lows,facecolor='purple',alpha=0.1)
    #设置图形的格式
    plt.title("Daily high and low temperatures- 2014",fontsize = 24)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)",fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()