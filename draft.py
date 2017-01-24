import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter
import operator
import collections


data = pd.read_csv('database.csv')

dates = []
start = 0
while start < len(data):
    date = datetime.strptime(data.iat[start, 2], "%Y-%m-%d")
    race = data.iat[start, 7]
    if race == 'B':

        dates.append(date)
    start += 1
number_deaths = Counter(dates)
sorted_values = collections.OrderedDict(sorted(number_deaths.items()))
dates = []
deaths = []
for item in sorted_values:
    dates.append(item)
    deaths.append(sorted_values[item])

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, deaths, linewidth=2, c="red")
plt.title("African American Deaths from Police", fontsize=24)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Deaths", fontsize=16)
plt.show()







##### Scrap #######

#race = data.iat[start, 7]

# if race =='B':
#     print('Asian')


#print(data.iat[start, 7])
