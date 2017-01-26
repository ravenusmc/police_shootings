import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter
import operator
import collections


data = pd.read_csv('database.csv')



black = data[data.race == 'B']
white = data[data.race == 'W']
black_count = len(black)
white_count = len(white)
print('length:', len(data))
#black = data[(data.armed == 'unarmed')  & (data.race == 'B')]
white = data[(data.armed == 'unarmed') & (data.race == 'W')]
print(white.head())
