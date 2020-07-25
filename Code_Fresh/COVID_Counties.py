import pandas as pd 
import os

covid_path = '/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/COVID/RAW_DATA/'
CC_AQI_path = '/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/AQI/CC_AP_AQI/'

cases = pd.read_csv(covid_path+'time_series_covid19_confirmed_US.csv')
deaths = pd.read_csv(covid_path+'time_series_covid19_deaths_US.csv')

AQI_sample = pd.read_csv(CC_AQI_path+'2019_CC_AP_AQI.csv')

counties = list(AQI_sample['StateCounty'])
cases = cases[cases['Combined_Key'].isin(counties)]
deaths = deaths[deaths['Combined_Key'].isin(counties)]

covid_out_path = '/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/COVID/CC_COVID/'
cases.to_csv(covid_out_path+'Confirmed_Cases_CC.csv', index = False)
deaths.to_csv(covid_out_path+'Deaths_CC.csv', index = False)

final_counties = list(cases['Combined_Key'])

files = os.listdir(CC_AQI_path)
for file in files: 
	df = pd.read_csv(CC_AQI_path+file)
	df = df[df['StateCounty'].isin(final_counties)]
	df.to_csv(CC_AQI_path+file, index = False)
