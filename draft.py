import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter
import operator
import collections


#I have an error somewhere in my data so I am trying to find it. I am going through the 
#total_police_deaths method to find it.


data = pd.read_csv('database.csv')



black = data[data.race == 'B']
white = data[data.race == 'W']
black_count = len(black)
white_count = len(white)
print('length:', len(data))
#black = data[(data.armed == 'unarmed')  & (data.race == 'B')]
white = data[(data.armed == 'unarmed') & (data.race == 'W')]
print(white.head())
