import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


data = pd.read_csv('database.csv')

black_deaths = []
dates = []
start = 0
black_count = 0

while start < 1948:
    date = datetime.strptime(data.iat[start, 2], "%Y-%m-%d")
    race = data.iat[start, 7]
    if race == 'B':
        black_count += 1
        black_deaths.append(black_count)
        dates.append(date)
    start += 1

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, black_deaths, linewidth=2, c="red")
plt.title("Deaths", fontsize=24)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Deaths", fontsize=16)
plt.show()

##### Scrap #######

#race = data.iat[start, 7]

# if race =='B':
#     print('Asian')


#print(data.iat[start, 7])
