import datetime

start = datetime.datetime(2019,9,1)
over = datetime.datetime(2022,6,14)

days_number = str(over-start)
day_data = int(days_number[0:4])
print("我们在一起已经：",day_data,"天啦！")
