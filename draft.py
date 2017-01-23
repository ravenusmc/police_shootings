import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter
import operator
import collections


data = pd.read_csv('database.csv')

black_deaths = []
dates = []
start = 0
prev_start = -1
black_count = 0

# while start < 12:
#     date = datetime.strptime(data.iat[start, 2], "%Y-%m-%d")
#     previous_date = datetime.strptime(data.iat[prev_start, 2], "%Y-%m-%d")
#     start += 1
#     prev_start += 1


while start < 1948:
    date = datetime.strptime(data.iat[start, 2], "%Y-%m-%d")
    previous_date = datetime.strptime(data.iat[prev_start, 2], "%Y-%m-%d")
    race = data.iat[start, 7]
    if race == 'B':
        black_count += 1
        black_deaths.append(black_count)
        dates.append(date)
    start += 1
    prev_start += 1

# print(dates[1])
# previous_date = datetime.strptime(data.iat[0, 2], "%Y-%m-%d")
# print(previous_date)

# print(datetime.strptime(data.iat[8, 2], "%Y-%m-%d"))
#This code gets me the count at the specific location that I enter.
# print(dates.count(dates[2]))
values = Counter(dates)
sorted_values = collections.OrderedDict(sorted(values.items()))
#length of sorted_values is 355
# print(sorted_values)

# test = datetime.strptime(data.iat[12, 2], "%Y-%m-%d")
# if test in sorted_values.keys():
#     print(sorted_values[test])
dates = []
deaths = []
for item in sorted_values:
    dates.append(item)
    deaths.append(sorted_values[item])

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, deaths, linewidth=2, c="red")
plt.title("Deaths", fontsize=24)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Deaths", fontsize=16)
plt.show()

# date_count = 1
# previous = 0
# death_count = []
# while previous < 100:
#     if datetime.strptime(data.iat[date_count, 2], "%Y-%m-%d") != datetime.strptime(data.iat[previous, 2], "%Y-%m-%d"):
#         death_count.append(dates.count(dates[date_count]))
#     date_count += 1
#     previous += 1
# print(death_count)



# container = []
# test_count = 0
# search_count = 0
# search_value = dates[test_count]
# print(search_value)
# for date in dates:
#     search_value = dates[test_count]
#     print(search_value)
#     test_count += 1
#     if search_value == dates[test_count]:
#         search_count += 1
#         container.append(search_count)
# print(container)






##### Scrap #######

#race = data.iat[start, 7]

# if race =='B':
#     print('Asian')


#print(data.iat[start, 7])
