import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 

Adelaide_AQ = pd.read_csv('Datasets/Adelaide_AQ.csv', index_col = 0)
Adelaide_dates = set(Adelaide_AQ.index.values)

Brisbane_AQ = pd.read_csv('Datasets/Brisbane_AQ.csv', index_col = 0)
Brisbane_dates = set(Brisbane_AQ.index.values)

Melbourne_AQ = pd.read_csv('Datasets/Melbourne_AQ.csv', index_col = 0)
Melbourne_dates = set(Melbourne_AQ.index.values)

Perth_AQ = pd.read_csv('Datasets/Perth_AQ.csv', index_col = 0)
Perth_dates = set(Perth_AQ.index.values)

Sydney_AQ = pd.read_csv('Datasets/Sydney_AQ.csv', index_col = 0)
Sydney_dates = set(Sydney_AQ.index.values)

dates = list(Adelaide_dates.intersection(Brisbane_dates, Melbourne_dates, Perth_dates, Sydney_dates))
dates = sorted(dates)
dates = dates[721:len(dates)]

print(dates)

'''
dates = [x for x in dates if x[0]=='2']

Adelaide_AQ = Adelaide_AQ.loc[dates]
Brisbane_AQ = Brisbane_AQ.loc[dates]
Melbourne_AQ = Melbourne_AQ.loc[dates]
Perth_AQ = Perth_AQ.loc[dates]
Sydney_AQ = Sydney_AQ.loc[dates]


Adelaide_AQ_Values = Adelaide_AQ[' pm25'].to_list()
Adelaide_AQ_Values = [None if x == ' ' else int(x) for x in Adelaide_AQ_Values]

Brisbane_AQ_Values = Brisbane_AQ[' pm25'].to_list()
Brisbane_AQ_Values = [None if x == ' ' else int(x) for x in Brisbane_AQ_Values]

Melbourne_AQ_Values = Melbourne_AQ[' pm25'].to_list()
Melbourne_AQ_Values = [None if x == ' ' else int(x) for x in Melbourne_AQ_Values]

Perth_AQ_Values = Perth_AQ[' pm25'].to_list()
Perth_AQ_Values = [None if x == ' ' else int(x) for x in Perth_AQ_Values]

Sydney_AQ_Values = Sydney_AQ[' pm25'].to_list()
Sydney_AQ_Values = [None if x == ' ' else int(x) for x in Sydney_AQ_Values]


fig, ax = plt.subplots() 
ax.plot(dates, Adelaide_AQ_Values, label='Adelaide', color='green')
ax.plot(dates, Brisbane_AQ_Values, label='Brisbane', color='orange')
ax.plot(dates, Melbourne_AQ_Values, label='Melbourne', color='red')
ax.plot(dates, Perth_AQ_Values, label='Perth', color='purple')
ax.plot(dates, Sydney_AQ_Values, label='Sydney', color='blue')
plt.xlabel('Date')
plt.ylabel('Air Quality Index')
plt.title('Air Quality Index in Major Australian Cities 2020')

every_nth = 10
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)


fig.autofmt_xdate()
plt.legend()
plt.show()
'''
