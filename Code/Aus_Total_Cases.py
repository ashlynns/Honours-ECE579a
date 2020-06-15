import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 


time_series_data = pd.read_csv('Datasets/time_series_covid19_confirmed_global.csv', index_col = 0)
aus_time_series_data = time_series_data[time_series_data['Country/Region']=='Australia']

aus_time_series_data = aus_time_series_data.drop(['Country/Region', 'Lat', 'Long'], axis = 1)
#print(aus_time_series_data)

x_axis = list(aus_time_series_data.columns.values)
ACT = list(aus_time_series_data.loc['Australian Capital Territory'])
NSW = list(aus_time_series_data.loc['New South Wales'])
NT = list(aus_time_series_data.loc['Northern Territory'])
Queensland = list(aus_time_series_data.loc['Queensland'])
SA = list(aus_time_series_data.loc['South Australia'])
Tasmania = list(aus_time_series_data.loc['Tasmania'])
Victoria = list(aus_time_series_data.loc['Victoria'])
WA = list(aus_time_series_data.loc['Western Australia'])

fig, ax = plt.subplots() 
ax.plot(x_axis, ACT, label='Australian Capital Territory')
ax.plot(x_axis, NSW, label='New South Wales')
ax.plot(x_axis, NT, label='Northern Territory')
ax.plot(x_axis, Queensland, label='Queensland')
ax.plot(x_axis, SA, label='South Australia')
ax.plot(x_axis, Tasmania, label='Tasmania')
ax.plot(x_axis, Victoria, label='Victoria')
ax.plot(x_axis, WA, label='Western Australia')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title('Total Australian COVID Cases')

every_nth = 10
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)

fig.autofmt_xdate()
plt.legend()
plt.show()