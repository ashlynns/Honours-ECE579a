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

a_dict = {}
b_dict={}
m_dict={}
p_dict ={}
s_dict = {}
for i, date in enumerate(dates):
	a = max(adelaide_pm25[i], adelaide_pm10[i], adelaide_co[i], adelaide_no2[i], adelaide_o3[i], adelaide_so2[i])
	a_dict[date]=a

	b = max(brisbane_pm25[i], brisbane_pm10[i], brisbane_co[i], brisbane_no2[i], brisbane_o3[i], brisbane_so2[i])
	b_dict[date]=b

	m = max(melbourne_pm25[i], melbourne_pm10[i], melbourne_co[i], melbourne_no2[i], melbourne_o3[i], melbourne_so2[i])
	m_dict[date]=m

	p = max(perth_pm25[i], perth_pm10[i], perth_co[i], perth_no2[i], perth_o3[i], perth_so2[i])
	p_dict[date]=p

	s = max(sydney_pm25[i], sydney_pm10[i], sydney_co[i], sydney_no2[i], sydney_o3[i], sydney_so2[i])
	s_dict[date]=s

every_nth = 10
fig1, ax1 = plt.subplots() 
ax1.plot(dates, list(a_dict.values()), label='Adelaide', color = 'green')
ax1.plot(dates, list(b_dict.values()), label='Brisbane', color = 'orange')
ax1.plot(dates, list(m_dict.values()), label='Melbourne', color = 'red')
ax1.plot(dates, list(p_dict.values()), label='Perth', color = 'purple')
ax1.plot(dates, list(s_dict.values()), label='Sydney', color = 'blue')
ax1.set_title('Average AQ Across Major Australian Cities')
ax1.set_xlabel('Date')
ax1.set_ylabel('Average AQ')
for n, label in enumerate(ax1.xaxis.get_ticklabels()):
   if n % every_nth != 0:
        label.set_visible(False)
fig1.autofmt_xdate()
plt.legend()
plt.show()

output_df = pd.DataFrame(index = dates)
output_df['Adelaide'] = a_dict.values()
output_df['Brisbane'] = b_dict.values()
output_df['Melbourne'] = m_dict.values()
output_df['Perth'] = p_dict.values()
output_df['Sydney'] = s_dict.values()

output_df.to_csv('Datasets/Average_AQ.csv')
