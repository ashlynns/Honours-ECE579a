import pandas as pd 
from datetime import date
import numpy as np

dates = pd.date_range(start='2019-08-01', end = '2020-05-01', freq='D').values
dates = [str(x)[0:10] for x in dates]

############## Adelaide ################
a1 = pd.read_csv('Datasets/Adelaide/adelaide-cbd, australia-air-quality.csv')
a1['date'] = pd.to_datetime(a1['date'])
a1.set_index('date', inplace = True)
a1 = a1[a1[' pm10']!=' ']

a2 = pd.read_csv('Datasets/Adelaide/north-western adelaide le fevre 1, australia-air-quality.csv')
a2['date'] = pd.to_datetime(a2['date'])
a2.set_index('date', inplace = True)
a2 = a2[a2[' pm10']!=' ']

a3 = pd.read_csv('Datasets/Adelaide/southern-adelaide christies, australia-air-quality.csv')
a3['date'] = pd.to_datetime(a3['date'])
a3.set_index('date', inplace = True)
a3 = a3[a3[' pm10']!=' ']

a4 = pd.read_csv('Datasets/Adelaide/western-adelaide netley, australia-air-quality.csv')
a4['date'] = pd.to_datetime(a4['date'])
a4.set_index('date', inplace = True)
a4 = a4[a4[' pm10']!=' ']

a_dict = {}
for date in dates:
	c, t1, t2, t3, t4 = 0, 0, 0, 0, 0
	if date in a1.index:
		t1 = int(a1.loc[date,' pm10'])
		c +=1
	if date in a2.index:
		t2 = int(a2.loc[date,' pm10'])
		c+=1
	if date in a3.index:
		t3 = int(a3.loc[date,' pm10'])
		c+=1
	if date in a4.index:
		t4 = int(a4.loc[date,' pm10'])
		c+=1
	if c ==0:
		a_dict[date]= None 
	if c !=0:
		a_dict[date]= (t1+t2+t3+t4)/c

############## Brisbane ################
b1 = pd.read_csv('Datasets/Brisbane/brisbane-cbd, australia-air-quality.csv')
b1['date'] = pd.to_datetime(b1['date'])
b1.set_index('date', inplace = True)
b1 = b1[b1[' pm10']!=' ']

b2 = pd.read_csv('Datasets/Brisbane/cannon-hill, australia-air-quality.csv')
b2['date'] = pd.to_datetime(b2['date'])
b2.set_index('date', inplace = True)
b2 = b2[b2[' pm10']!=' ']

b3 = pd.read_csv('Datasets/Brisbane/lytton,-australia-air-quality.csv')
b3['date'] = pd.to_datetime(b3['date'])
b3.set_index('date', inplace = True)
b3 = b3[b3[' pm10']!=' ']

b4 = pd.read_csv('Datasets/Brisbane/rocklea,-australia-air-quality.csv')
b4['date'] = pd.to_datetime(b4['date'])
b4.set_index('date', inplace = True)
b4 = b4[b4[' pm10']!=' ']

b5 = pd.read_csv('Datasets/Brisbane/south-brisbane, australia-air-quality.csv')
b5['date'] = pd.to_datetime(b5['date'])
b5.set_index('date', inplace = True)
b5 = b5[b5[' pm10']!=' ']

b6 = pd.read_csv('Datasets/Brisbane/springwood,-australia-air-quality.csv')
b6['date'] = pd.to_datetime(b6['date'])
b6.set_index('date', inplace = True)
b6 = b6[b6[' pm10']!=' ']

b7 = pd.read_csv('Datasets/Brisbane/woolloongabba,-australia-air-quality.csv')
b7['date'] = pd.to_datetime(b7['date'])
b7.set_index('date', inplace = True)
b7 = b7[b7[' pm10']!=' ']

b8 = pd.read_csv('Datasets/Brisbane/wynnum-west, australia-air-quality.csv')
b8['date'] = pd.to_datetime(b8['date'])
b8.set_index('date', inplace = True)
b8 = b8[b8[' pm10']!=' ']

b9 = pd.read_csv('Datasets/Brisbane/wynnum,-australia-air-quality.csv')
b9['date'] = pd.to_datetime(b9['date'])
b9.set_index('date', inplace = True)
b9 = b9[b9[' pm10']!=' ']

b_dict = {}
for date in dates:
	c, t1, t2, t3, t4, t5, t6, t7, t8, t9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	if date in b1.index:
		t1 = int(b1.loc[date,' pm10'])
		c +=1
	if date in b2.index:
		t2 = int(b2.loc[date,' pm10'])
		c+=1
	if date in b3.index:
		t3 = int(b3.loc[date,' pm10'])
		c+=1
	if date in b4.index:
		t4 = int(b4.loc[date,' pm10'])
		c+=1
	if date in b5.index:
		t5 = int(b5.loc[date,' pm10'])
		c+=1
	if date in b6.index:
		t6 = int(b6.loc[date,' pm10'])
		c+=1
	if date in b7.index:
		t7 = int(b7.loc[date,' pm10'])
		c+=1
	if date in b8.index:
		t8 = int(b8.loc[date,' pm10'])
		c+=1
	if date in b9.index:
		t9 = int(b9.loc[date,' pm10'])
		c+=1
	if c ==0:
		b_dict[date]= None 
	if c !=0:
		b_dict[date]= (t1+t2+t3+t4+t5+t6+t7+t8+t9)/c

############## Melbourne ################
m1 = pd.read_csv('Datasets/Melbourne/alphington,-australia-air-quality.csv')
m1['date'] = pd.to_datetime(m1['date'])
m1.set_index('date', inplace = True)
m1 = m1[m1[' pm10']!=' ']

m2 = pd.read_csv('Datasets/Melbourne/box-hill, australia-air-quality.csv')
m2['date'] = pd.to_datetime(m2['date'])
m2.set_index('date', inplace = True)
m2 = m2[m2[' pm10']!=' ']

m3 = pd.read_csv('Datasets/Melbourne/brighton,-australia-air-quality.csv')
m3['date'] = pd.to_datetime(m3['date'])
m3.set_index('date', inplace = True)
m3 = m3[m3[' pm10']!=' ']

m4 = pd.read_csv('Datasets/Melbourne/brooklyn,-australia-air-quality.csv')
m4['date'] = pd.to_datetime(m4['date'])
m4.set_index('date', inplace = True)
m4 = m4[m4[' pm10']!=' ']

m5 = pd.read_csv('Datasets/Melbourne/campbellfield-air-quality.csv')
m5['date'] = pd.to_datetime(m5['date'])
m5.set_index('date', inplace = True)
m5 = m5[m5[' pm10']!=' ']

m6 = pd.read_csv('Datasets/Melbourne/dallas,-australia-air-quality.csv')
m6['date'] = pd.to_datetime(m6['date'])
m6.set_index('date', inplace = True)
m6 = m6[m6[' pm10']!=' ']

m7 = pd.read_csv('Datasets/Melbourne/dandenong,-australia-air-quality.csv')
m7['date'] = pd.to_datetime(m7['date'])
m7.set_index('date', inplace = True)
m7 = m7[m7[' pm10']!=' ']

m8 = pd.read_csv('Datasets/Melbourne/footscray,-australia-air-quality.csv')
m8['date'] = pd.to_datetime(m8['date'])
m8.set_index('date', inplace = True)
m8 = m8[m8[' pm10']!=' ']

m9 = pd.read_csv('Datasets/Melbourne/macleod,-australia-air-quality.csv')
m9['date'] = pd.to_datetime(m9['date'])
m9.set_index('date', inplace = True)
m9 = m9[m9[' pm10']!=' ']

m10 = pd.read_csv('Datasets/Melbourne/melbourne-cbd, australia-air-quality.csv')
m10['date'] = pd.to_datetime(m10['date'])
m10.set_index('date', inplace = True)
m10 = m10[m10[' pm10']!=' ']

m11 = pd.read_csv('Datasets/Melbourne/pt.-cook, australia-air-quality.csv')
m11['date'] = pd.to_datetime(m11['date'])
m11.set_index('date', inplace = True)
m11 = m11[m11[' pm10']!=' ']

m_dict = {}
for date in dates:
	c, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	if date in m1.index:
		t1 = int(m1.loc[date,' pm10'])
		c +=1
	if date in m2.index:
		t2 = int(m2.loc[date,' pm10'])
		c+=1
	if date in m3.index:
		t3 = int(m3.loc[date,' pm10'])
		c+=1
	if date in m4.index:
		t4 = int(m4.loc[date,' pm10'])
		c+=1
	if date in m5.index:
		t5 = int(m5.loc[date,' pm10'])
		c+=1
	if date in m6.index:
		t6 = int(m6.loc[date,' pm10'])
		c+=1
	if date in m7.index:
		t7 = int(m7.loc[date,' pm10'])
		c+=1
	if date in m8.index:
		t8 = int(m8.loc[date,' pm10'])
		c+=1
	if date in m9.index:
		t9 = int(m9.loc[date,' pm10'])
		c+=1
	if date in m10.index:
		t10 = int(m10.loc[date,' pm10'])
		c+=1
	if date in m11.index:
		t11 = int(m11.loc[date,' pm10'])
		c+=1
	if c ==0:
		m_dict[date]= None 
	if c !=0:
		m_dict[date]= (t1+t2+t3+t4+t5+t6+t7+t8+t9+t10+t11)/c


############## Perth ################
p1 = pd.read_csv('Datasets/Perth/caversham,-australia-air-quality.csv')
p1['date'] = pd.to_datetime(p1['date'])
p1.set_index('date', inplace = True)
p1 = p1[p1[' pm10']!=' ']

p2 = pd.read_csv('Datasets/Perth/duncraig,-australia-air-quality.csv')
p2['date'] = pd.to_datetime(p2['date'])
p2.set_index('date', inplace = True)
p2 = p2[p2[' pm10']!=' ']

p3 = pd.read_csv('Datasets/Perth/quinns-rocks, australia-air-quality.csv')
p3['date'] = pd.to_datetime(p3['date'])
p3.set_index('date', inplace = True)
p3 = p3[p3[' pm10']!=' ']

p4 = pd.read_csv('Datasets/Perth/south-lake, australia-air-quality.csv')
p4['date'] = pd.to_datetime(p4['date'])
p4.set_index('date', inplace = True)
p4 = p4[p4[' pm10']!=' ']

p_dict = {}
for date in dates:
	c, t1, t2, t3, t4 = 0, 0, 0, 0, 0
	if date in p1.index:
		t1 = int(p1.loc[date,' pm10'])
		c +=1
	if date in p2.index:
		t2 = int(p2.loc[date,' pm10'])
		c+=1
	if date in p3.index:
		t3 = int(p3.loc[date,' pm10'])
		c+=1
	if date in p4.index:
		t4 = int(p4.loc[date,' pm10'])
		c+=1
	if c ==0:
		p_dict[date]= None 
	if c !=0:
		p_dict[date]= (t1+t2+t3+t4)/c

############## Sydney ################
s1 = pd.read_csv('Datasets/Sydney/bargo-sydney south-west, australia-air-quality.csv')
s1['date'] = pd.to_datetime(s1['date'])
s1.set_index('date', inplace = True)
s1 = s1[s1[' pm10']!=' ']

s2 = pd.read_csv('Datasets/Sydney/bringelly-sydney south-west, australia-air-quality.csv')
s2['date'] = pd.to_datetime(s2['date'])
s2.set_index('date', inplace = True)
s2 = s2[s2[' pm10']!=' ']

s3 = pd.read_csv('Datasets/Sydney/camden-sydney south-west, australia-air-quality.csv')
s3['date'] = pd.to_datetime(s3['date'])
s3.set_index('date', inplace = True)
s3 = s3[s3[' pm10']!=' ']

s4 = pd.read_csv('Datasets/Sydney/chullora-sydney east, australia-air-quality.csv')
s4['date'] = pd.to_datetime(s4['date'])
s4.set_index('date', inplace = True)
s4 = s4[s4[' pm10']!=' ']

s5 = pd.read_csv('Datasets/Sydney/cook-and phillip sydney east, australia-air-quality.csv')
s5['date'] = pd.to_datetime(s5['date'])
s5.set_index('date', inplace = True)
s5 = s5[s5[' pm10']!=' ']

s6 = pd.read_csv('Datasets/Sydney/earlwood-sydney east, australia-air-quality.csv')
s6['date'] = pd.to_datetime(s6['date'])
s6.set_index('date', inplace = True)
s6 = s6[s6[' pm10']!=' ']

s7 = pd.read_csv('Datasets/Sydney/liverpool-sydney south-west, australia-air-quality.csv')
s7['date'] = pd.to_datetime(s7['date'])
s7.set_index('date', inplace = True)
s7 = s7[s7[' pm10']!=' ']

s8 = pd.read_csv('Datasets/Sydney/macquarie-park sydney east, australia-air-quality.csv')
s8['date'] = pd.to_datetime(s8['date'])
s8.set_index('date', inplace = True)
s8 = s8[s8[' pm10']!=' ']

s9 = pd.read_csv('Datasets/Sydney/north-parramatta sydney north-west, australia-air-quality.csv')
s9['date'] = pd.to_datetime(s9['date'])
s9.set_index('date', inplace = True)
s9 = s9[s9[' pm10']!=' ']

s10 = pd.read_csv('Datasets/Sydney/prospect-sydney north-west, australia-air-quality.csv')
s10['date'] = pd.to_datetime(s10['date'])
s10.set_index('date', inplace = True)
s10 = s10[s10[' pm10']!=' ']

s11 = pd.read_csv('Datasets/Sydney/randwick-sydney east, australia-air-quality.csv')
s11['date'] = pd.to_datetime(s11['date'])
s11.set_index('date', inplace = True)
s11 = s11[s11[' pm10']!=' ']

s12 = pd.read_csv('Datasets/Sydney/richmond-sydney north-west, australia-air-quality.csv')
s12['date'] = pd.to_datetime(s12['date'])
s12.set_index('date', inplace = True)
s12 = s12[s12[' pm10']!=' ']

s13 = pd.read_csv('Datasets/Sydney/rouse-hill sydney north-west, australia-air-quality.csv')
s13['date'] = pd.to_datetime(s13['date'])
s13.set_index('date', inplace = True)
s13 = s13[s13[' pm10']!=' ']

s14 = pd.read_csv('Datasets/Sydney/rozelle-sydney east, australia-air-quality.csv')
s14['date'] = pd.to_datetime(s14['date'])
s14.set_index('date', inplace = True)
s14 = s14[s14[' pm10']!=' ']

s15 = pd.read_csv('Datasets/Sydney/st-marys sydney north-west, australia-air-quality.csv')
s15['date'] = pd.to_datetime(s15['date'])
s15.set_index('date', inplace = True)
s15 = s15[s15[' pm10']!=' ']

s_dict = {}
for date in dates:
	c, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	if date in s1.index:
		t1 = int(s1.loc[date,' pm10'])
		c +=1
	if date in s2.index:
		t2 = int(s2.loc[date,' pm10'])
		c+=1
	if date in s3.index:
		t3 = int(s3.loc[date,' pm10'])
		c+=1
	if date in s4.index:
		t4 = int(s4.loc[date,' pm10'])
		c+=1
	if date in s5.index:
		t5 = int(s5.loc[date,' pm10'])
		c+=1
	if date in s6.index:
		t6 = int(s6.loc[date,' pm10'])
		c+=1
	if date in s7.index:
		t7 = int(s7.loc[date,' pm10'])
		c+=1
	if date in s8.index:
		t8 = int(s8.loc[date,' pm10'])
		c+=1
	if date in s9.index:
		t9 = int(s9.loc[date,' pm10'])
		c+=1
	if date in s10.index:
		t10 = int(s10.loc[date,' pm10'])
		c+=1
	if date in s11.index:
		t11 = int(s11.loc[date,' pm10'])
		c+=1
	if date in s12.index:
		t12 = int(s12.loc[date,' pm10'])
		c+=1
	if date in s13.index:
		t13 = int(s13.loc[date,' pm10'])
		c+=1
	if date in s14.index:
		t14 = int(s14.loc[date,' pm10'])
		c+=1
	if date in s15.index:
		t15 = int(s15.loc[date,' pm10'])
		c+=1
	if c ==0:
		s_dict[date]= None 
	if c !=0:
		s_dict[date]= (t1+t2+t3+t4+t5+t6+t7+t8+t9+t10+t11+t12+t13+t14+t15)/c

########### Dataframe Creation ############
output_df = pd.DataFrame(index = dates)
output_df['Adelaide'] = a_dict.values()
output_df['Brisbane'] = b_dict.values()
output_df['Melbourne'] = m_dict.values()
output_df['Perth'] = p_dict.values()
output_df['Sydney'] = s_dict.values()

output_df.to_csv('Datasets/Average_pm10.csv')




