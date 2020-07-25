import pandas as pd 
import os 

CC_AP_AQI_path = '/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/AQI/CC_AP_AQI/'

AQI_2019 = pd.read_csv(CC_AP_AQI_path+'2019_CC_AP_AQI.csv')
AQI_2018 = pd.read_csv(CC_AP_AQI_path+'2018_CC_AP_AQI.csv')
AQI_2017 = pd.read_csv(CC_AP_AQI_path+'2017_CC_AP_AQI.csv')
AQI_2016 = pd.read_csv(CC_AP_AQI_path+'2016_CC_AP_AQI.csv')
AQI_2015 = pd.read_csv(CC_AP_AQI_path+'2015_CC_AP_AQI.csv')
AQI_2014 = pd.read_csv(CC_AP_AQI_path+'2014_CC_AP_AQI.csv')

col = ['State','County','Good Days', 'Moderate Days','Unhealthy for Sensitive Groups Days','Unhealthy Days', 'Very Unhealthy Days' , 'Hazardous Days']
State = AQI_2019['State']
County = AQI_2019['County']
Good_Days = (AQI_2019['Good Days']+AQI_2018['Good Days']+AQI_2017['Good Days']+AQI_2016['Good Days']+AQI_2015['Good Days']+AQI_2014['Good Days'])/6
Moderate_Days = (AQI_2019['Moderate Days']+AQI_2018['Moderate Days']+AQI_2017['Moderate Days']+AQI_2016['Moderate Days']+AQI_2015['Moderate Days']+AQI_2014['Moderate Days'])/6
Unhealthy_for_Sensitive_Groups_Days = (AQI_2019['Unhealthy for Sensitive Groups Days']+AQI_2018['Unhealthy for Sensitive Groups Days']+AQI_2017['Unhealthy for Sensitive Groups Days']+AQI_2016['Unhealthy for Sensitive Groups Days']+AQI_2015['Unhealthy for Sensitive Groups Days']+AQI_2014['Unhealthy for Sensitive Groups Days'])/6
Unhealthy_Days = (AQI_2019['Unhealthy Days']+AQI_2018['Unhealthy Days']+AQI_2017['Unhealthy Days']+AQI_2016['Unhealthy Days']+AQI_2015['Unhealthy Days']+AQI_2014['Unhealthy Days'])/6
Very_Unhealthy_Days = (AQI_2019['Very Unhealthy Days']+AQI_2018['Very Unhealthy Days']+AQI_2017['Very Unhealthy Days']+AQI_2016['Very Unhealthy Days']+AQI_2015['Very Unhealthy Days']+AQI_2014['Very Unhealthy Days'])/6
Hazardous_Days = (AQI_2019['Hazardous Days']+AQI_2018['Hazardous Days']+AQI_2017['Hazardous Days']+AQI_2016['Hazardous Days']+AQI_2015['Hazardous Days']+AQI_2014['Hazardous Days'])/6

Combined_AQI = pd.DataFrame()
Combined_AQI['State'] = State
Combined_AQI['County'] = County
Combined_AQI['Good Days'] = Good_Days
Combined_AQI['Moderate Days'] = Moderate_Days
Combined_AQI['Unhealthy for Sensitive Groups Days'] = Unhealthy_for_Sensitive_Groups_Days
Combined_AQI['Unhealthy Days'] = Unhealthy_Days
Combined_AQI['Very Unhealthy Days'] = Very_Unhealthy_Days
Combined_AQI['Hazardous Days'] = Hazardous_Days

Combined_AQI.to_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/AQI/Combined_AQI.csv', index = False)
