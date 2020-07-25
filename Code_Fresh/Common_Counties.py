import pandas as pd 

AQI_path = '/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/AQI/RAW_DATA/'

# Reading in all of the files 
AQI_2019 = pd.read_csv(AQI_path+'annual_aqi_by_county_2019.csv')
AQI_2018 = pd.read_csv(AQI_path+'annual_aqi_by_county_2018.csv')
AQI_2017 = pd.read_csv(AQI_path+'annual_aqi_by_county_2017.csv')
AQI_2016 = pd.read_csv(AQI_path+'annual_aqi_by_county_2016.csv')
AQI_2015 = pd.read_csv(AQI_path+'annual_aqi_by_county_2015.csv')
AQI_2014 = pd.read_csv(AQI_path+'annual_aqi_by_county_2014.csv')

AQI_2019 = AQI_2019[AQI_2019['Days with AQI']>180]
AQI_2018 = AQI_2018[AQI_2018['Days with AQI']>180]
AQI_2017 = AQI_2017[AQI_2017['Days with AQI']>180]
AQI_2016 = AQI_2016[AQI_2016['Days with AQI']>180]
AQI_2015 = AQI_2015[AQI_2015['Days with AQI']>180]
AQI_2014 = AQI_2014[AQI_2014['Days with AQI']>180]

# Adding a column for state & county since county names are not a unique identifier 
AQI_2019['StateCounty'] = AQI_2019['County']+', '+AQI_2019['State']+', US'
AQI_2018['StateCounty'] = AQI_2018['County']+', '+AQI_2018['State']+', US'
AQI_2017['StateCounty'] = AQI_2017['County']+', '+AQI_2017['State']+', US'
AQI_2016['StateCounty'] = AQI_2016['County']+', '+AQI_2016['State']+', US'
AQI_2015['StateCounty'] = AQI_2015['County']+', '+AQI_2015['State']+', US'
AQI_2014['StateCounty'] = AQI_2014['County']+', '+AQI_2014['State']+', US'

# Creating a set for the statecounty column from each file to use the intersection function 
SC_2019 = set(AQI_2019['StateCounty'])
SC_2018 = set(AQI_2018['StateCounty'])
SC_2017 = set(AQI_2017['StateCounty'])
SC_2016 = set(AQI_2016['StateCounty'])
SC_2015 = set(AQI_2015['StateCounty'])
SC_2014 = set(AQI_2014['StateCounty'])

# Generating a list of all the common counties
Common_SC = SC_2019.intersection(SC_2018, SC_2017,SC_2016, SC_2015, SC_2014)

# Removing all of the counties that arent in all the datasets 
# Also reindexing the new dataframes bc i dont trust anything
AQI_2019 = AQI_2019[AQI_2019['StateCounty'].isin(Common_SC)]
AQI_2019 = AQI_2019.reset_index(drop=True)

AQI_2018 = AQI_2018[AQI_2018['StateCounty'].isin(Common_SC)]
AQI_2018 = AQI_2018.reset_index(drop=True)

AQI_2017 = AQI_2017[AQI_2017['StateCounty'].isin(Common_SC)]
AQI_2017 = AQI_2017.reset_index(drop=True)

AQI_2016 = AQI_2016[AQI_2016['StateCounty'].isin(Common_SC)]
AQI_2016 = AQI_2016.reset_index(drop=True)

AQI_2015 = AQI_2015[AQI_2015['StateCounty'].isin(Common_SC)]
AQI_2015 = AQI_2015.reset_index(drop=True)

AQI_2014 = AQI_2014[AQI_2014['StateCounty'].isin(Common_SC)]
AQI_2014 = AQI_2014.reset_index(drop=True)

# Turns the absolute number of days in a given group into a percentage relative to the number of measurments
def as_percent(df):
	days = df['Days with AQI']
	df['Good Days'] = df['Good Days']/days
	df['Moderate Days'] = df['Moderate Days']/days
	df['Unhealthy for Sensitive Groups Days'] = df['Unhealthy for Sensitive Groups Days']/days
	df['Unhealthy Days'] = df['Unhealthy Days']/days
	df['Very Unhealthy Days'] = df['Very Unhealthy Days']/days
	df['Hazardous Days'] = df['Hazardous Days']/days
	df['Days CO'] = df['Days CO']/days
	df['Days NO2'] = df['Days NO2']/days 
	df['Days Ozone'] = df['Days Ozone']/days 
	df['Days SO2'] = df['Days SO2']/days 
	df['Days PM2.5'] = df['Days PM2.5']/days 
	df['Days PM10']=df['Days PM10']/days
	return(df)

AQI_2019_AP = as_percent(AQI_2019)
AQI_2018_AP = as_percent(AQI_2018)
AQI_2017_AP = as_percent(AQI_2017)
AQI_2016_AP = as_percent(AQI_2016)
AQI_2015_AP = as_percent(AQI_2015)
AQI_2014_AP = as_percent(AQI_2014)

CC_AP_AQI_path = '/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/AQI/CC_AP_AQI/'
AQI_2019_AP.to_csv(CC_AP_AQI_path+'2019_CC_AP_AQI.csv', index = False)
AQI_2018_AP.to_csv(CC_AP_AQI_path+'2018_CC_AP_AQI.csv', index = False)
AQI_2017_AP.to_csv(CC_AP_AQI_path+'2017_CC_AP_AQI.csv', index = False)
AQI_2016_AP.to_csv(CC_AP_AQI_path+'2016_CC_AP_AQI.csv', index = False)
AQI_2015_AP.to_csv(CC_AP_AQI_path+'2015_CC_AP_AQI.csv', index = False)
AQI_2014_AP.to_csv(CC_AP_AQI_path+'2014_CC_AP_AQI.csv', index = False)
