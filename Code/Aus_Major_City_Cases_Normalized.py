import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 


time_series_data = pd.read_csv('Datasets/time_series_covid19_confirmed_global.csv', index_col = 0)
aus_time_series_data = time_series_data[time_series_data['Country/Region']=='Australia']

aus_time_series_data = aus_time_series_data.drop(['Country/Region', 'Lat', 'Long'], axis = 1)

Sydney_population = 5230330
Melbourne_population = 4936349
Brisbane_population = 2462637
Perth_population = 2059484
Adelaide_population = 1345777

x_axis = list(aus_time_series_data.columns.values)
NSW_true = list(aus_time_series_data.loc['New South Wales']) # Sydney
NSW = [x/Sydney_population for x in NSW_true]
Queensland_true = list(aus_time_series_data.loc['Queensland']) # Brisbane
Queensland = [x/Brisbane_population for x in Queensland_true] 
SA_true = list(aus_time_series_data.loc['South Australia']) # Adelaide
SA = [x/Adelaide_population for x in SA_true]
Victoria_true = list(aus_time_series_data.loc['Victoria']) # Melbourne
Victoria = [x/Melbourne_population for x in Victoria_true] 
WA_true = list(aus_time_series_data.loc['Western Australia']) # Perth
WA = [x/Perth_population for x in WA_true]

fig, ax = plt.subplots() 
ax.plot(x_axis, NSW, label='New South Wales', color='blue')
ax.plot(x_axis, Queensland, label='Queensland', color='orange')
ax.plot(x_axis, SA, label='South Australia', color='green')
ax.plot(x_axis, Victoria, label='Victoria', color='red')
ax.plot(x_axis, WA, label='Western Australia', color='purple')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title('Australian States with Major Cities COVID Cases - Nomalized by Population')

every_nth = 10
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)

fig.autofmt_xdate()
plt.legend()
plt.show()
