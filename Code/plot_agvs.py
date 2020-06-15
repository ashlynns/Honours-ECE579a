import pandas as pd 
from datetime import date
import numpy as np
import matplotlib.pyplot as plt

avg_AQ = pd.read_csv('Datasets/Average_AQ.csv', index_col =0)
dates = list(avg_AQ.index.values)

adelaide = list(avg_AQ['Adelaide'])
brisbane = list(avg_AQ['Brisbane'])
melbourne = list(avg_AQ['Melbourne'])
perth = list(avg_AQ['Perth'])
sydney = list(avg_AQ['Sydney'])

fig, ax = plt.subplots() 
ax.plot(dates, adelaide, label='Adelaide', color = 'green')
ax.plot(dates, brisbane, label='Brisbane', color = 'orange')
ax.plot(dates, melbourne, label='Melbourne', color = 'red')
ax.plot(dates, perth, label='Perth', color = 'purple')
ax.plot(dates, sydney, label='Sydney', color = 'blue')

plt.xlabel('Date')
plt.ylabel('Average City AQ (pm25)')
plt.title('Average pm25 Across Major Australian Cities')

every_nth = 10
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)

fig.autofmt_xdate()
plt.legend()
plt.show()


