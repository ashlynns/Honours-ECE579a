import pandas as pd 
from datetime import date
import numpy as np
import matplotlib.pyplot as plt

avg_pm25 = pd.read_csv('Datasets/Average_pm25.csv', index_col =0)
avg_pm10 = pd.read_csv('Datasets/Average_pm10.csv', index_col =0)
avg_co = pd.read_csv('Datasets/Average_co.csv', index_col =0)
avg_no2 = pd.read_csv('Datasets/Average_no2.csv', index_col =0)
avg_o3 = pd.read_csv('Datasets/Average_o3.csv', index_col =0)
avg_so2 = pd.read_csv('Datasets/Average_so2.csv', index_col =0)
dates = list(avg_pm25.index.values)

adelaide_pm25 = list(avg_pm25['Adelaide'])
brisbane_pm25 = list(avg_pm25['Brisbane'])
melbourne_pm25 = list(avg_pm25['Melbourne'])
perth_pm25 = list(avg_pm25['Perth'])
sydney_pm25 = list(avg_pm25['Sydney'])

adelaide_pm10 = list(avg_pm10['Adelaide'])
brisbane_pm10 = list(avg_pm10['Brisbane'])
melbourne_pm10 = list(avg_pm10['Melbourne'])
perth_pm10 = list(avg_pm10['Perth'])
sydney_pm10 = list(avg_pm10['Sydney'])

adelaide_co = list(avg_co['Adelaide'])
brisbane_co = list(avg_co['Brisbane'])
melbourne_co = list(avg_co['Melbourne'])
perth_co = list(avg_co['Perth'])
sydney_co = list(avg_co['Sydney'])

adelaide_no2 = list(avg_no2['Adelaide'])
brisbane_no2 = list(avg_no2['Brisbane'])
melbourne_no2 = list(avg_no2['Melbourne'])
perth_no2 = list(avg_no2['Perth'])
sydney_no2 = list(avg_no2['Sydney'])

adelaide_o3 = list(avg_o3['Adelaide'])
brisbane_o3 = list(avg_o3['Brisbane'])
melbourne_o3 = list(avg_o3['Melbourne'])
perth_o3 = list(avg_o3['Perth'])
sydney_o3 = list(avg_o3['Sydney'])

adelaide_so2 = list(avg_so2['Adelaide'])
brisbane_so2 = list(avg_so2['Brisbane'])
melbourne_so2 = list(avg_so2['Melbourne'])
perth_so2 = list(avg_so2['Perth'])
sydney_so2 = list(avg_so2['Sydney'])

every_nth = 10

#PM25
fig1, ax1 = plt.subplots() 
ax1.plot(dates, adelaide_pm25, label='Adelaide', color = 'green')
ax1.plot(dates, brisbane_pm25, label='Brisbane', color = 'orange')
ax1.plot(dates, melbourne_pm25, label='Melbourne', color = 'red')
ax1.plot(dates, perth_pm25, label='Perth', color = 'purple')
ax1.plot(dates, sydney_pm25, label='Sydney', color = 'blue')
ax1.set_title('Average pm25 Across Major Australian Cities')
ax1.set_xlabel('Date')
ax1.set_ylabel('Average pm25')
for n, label in enumerate(ax1.xaxis.get_ticklabels()):
   if n % every_nth != 0:
        label.set_visible(False)
fig1.autofmt_xdate()
fig1.legend()

#PM10
fig2, ax2 = plt.subplots()
ax2.plot(dates, adelaide_pm10, label='Adelaide', color = 'green')
ax2.plot(dates, brisbane_pm10, label='Brisbane', color = 'orange')
ax2.plot(dates, melbourne_pm10, label='Melbourne', color = 'red')
ax2.plot(dates, perth_pm10, label='Perth', color = 'purple')
ax2.plot(dates, sydney_pm10, label='Sydney', color = 'blue')
ax2.set_title('Average pm10 Across Major Australian Cities')
ax2.set_xlabel('Date')
ax2.set_ylabel('Average pm10')
for n, label in enumerate(ax2.xaxis.get_ticklabels()):
   if n % every_nth != 0:
        label.set_visible(False)
fig2.autofmt_xdate()
fig2.legend()

#CO
fig3, ax3 = plt.subplots()
ax3.plot(dates, adelaide_co, label='Adelaide', color = 'green')
ax3.plot(dates, brisbane_co, label='Brisbane', color = 'orange')
ax3.plot(dates, melbourne_co, label='Melbourne', color = 'red')
ax3.plot(dates, perth_co, label='Perth', color = 'purple')
ax3.plot(dates, sydney_co, label='Sydney', color = 'blue')
ax3.set_title('Average CO Across Major Australian Cities')
ax3.set_xlabel('Date')
ax3.set_ylabel('Average CO')
for n, label in enumerate(ax3.xaxis.get_ticklabels()):
   if n % every_nth != 0:
        label.set_visible(False)
fig3.autofmt_xdate()
fig3.legend()

#NO2
fig4, ax4 = plt.subplots()
ax4.plot(dates, adelaide_no2, label='Adelaide', color = 'green')
ax4.plot(dates, brisbane_no2, label='Brisbane', color = 'orange')
ax4.plot(dates, melbourne_no2, label='Melbourne', color = 'red')
ax4.plot(dates, perth_no2, label='Perth', color = 'purple')
ax4.plot(dates, sydney_no2, label='Sydney', color = 'blue')
ax4.set_title('Average NO2 Across Major Australian Cities')
ax4.set_xlabel('Date')
ax4.set_ylabel('Average NO2')
for n, label in enumerate(ax4.xaxis.get_ticklabels()):
   if n % every_nth != 0:
        label.set_visible(False)
fig4.autofmt_xdate()
fig4.legend()

#O3
fig5, ax5 = plt.subplots()
ax5.plot(dates, adelaide_o3, label='Adelaide', color = 'green')
ax5.plot(dates, brisbane_o3, label='Brisbane', color = 'orange')
ax5.plot(dates, melbourne_o3, label='Melbourne', color = 'red')
ax5.plot(dates, perth_o3, label='Perth', color = 'purple')
ax5.plot(dates, sydney_o3, label='Sydney', color = 'blue')
ax5.set_title('Average O3 Across Major Australian Cities')
ax5.set_xlabel('Date')
ax5.set_ylabel('Average O3')
for n, label in enumerate(ax5.xaxis.get_ticklabels()):
   if n % every_nth != 0:
        label.set_visible(False)
fig5.autofmt_xdate()
fig5.legend()

# SO2
fig6, ax6 = plt.subplots()
ax6.plot(dates, adelaide_so2, label='Adelaide', color = 'green')
ax6.plot(dates, brisbane_so2, label='Brisbane', color = 'orange')
ax6.plot(dates, melbourne_so2, label='Melbourne', color = 'red')
ax6.plot(dates, perth_so2, label='Perth', color = 'purple')
ax6.plot(dates, sydney_so2, label='Sydney', color = 'blue')
ax6.set_title('Average SO2 Across Major Australian Cities')
ax6.set_xlabel('Date')
ax6.set_ylabel('Average SO2')
for n, label in enumerate(ax6.xaxis.get_ticklabels()):
   if n % every_nth != 0:
        label.set_visible(False)
fig6.autofmt_xdate()
fig6.legend()


plt.show()


