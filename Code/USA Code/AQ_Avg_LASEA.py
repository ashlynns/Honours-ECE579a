import pandas as pd 
import numpy as np 
import os 

Sea_path = '/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code/Datasets/USA/LASEA/King_County/'
LA_path = '/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code/Datasets/USA/LASEA/LA_County/'


def dates(path):
# Compiles a list of dates common to all datasets 	
	file_list = [x for x in os.listdir(path) if x.endswith('.csv')] # get all the files in the folder 
	dates = []
	for file in file_list: 
		file = path+file # path
		df = pd.read_csv(file)
		dates.append(set(df['date'])) # a list of sets of dates
	dates = dates[0].intersection(*dates) # find the intersection of all of the sets, aka the dates inculeded in every dataset
	return list(dates)


def AQ_Values_AVG(path):
	date_list = dates(path) # get common dates 
	file_list = [x for x in os.listdir(path) if x.endswith('.csv')]
	data_zeros = np.zeros((len(date_list),5), dtype=int)
	AVG_DF = pd.DataFrame(data_zeros, columns = [' pm25', ' o3', ' no2', ' so2', ' co']) # Initializing the AVG dataframe
	sorted_dates = []

	for file in file_list:
		file = path+file
		df = pd.read_csv(file, na_values = ' ')
		df = df[df['date'].isin(date_list)] # Keeping only the rows where the dates are common to all datasets 
		df = df.sort_values(by='date', ascending = False) # sort rows by dates so we are averaging across the correct days 
		sorted_dates = list(df['date'])
		df = df.reindex(range(len(df)))
		df = df.fillna(0) 

		# For each dataset add the value to the correct AVG_DF column 
		AVG_DF[' pm25'] = AVG_DF[' pm25'].astype('float')+df[' pm25'].astype('float')
		AVG_DF[' o3'] = AVG_DF[' o3'].astype('float')+df[' o3'].astype('float')
		AVG_DF[' no2'] = AVG_DF[' no2'].astype('float')+df[' no2'].astype('float')
		AVG_DF[' so2'] = AVG_DF[' so2'].astype('float')+df[' so2'].astype('float')
		AVG_DF[' co'] = AVG_DF[' co'].astype('float')+df[' co'].astype('float')

	AVG_DF = AVG_DF.divide(len(file_list)) # Divide all the entries but the number of datasets
	AVG_DF = AVG_DF.round() # Round the values 
	AVG_DF.insert(0, 'date', sorted_dates) # Add the date column 
	return AVG_DF

AVG_SEA_Data = AQ_Values_AVG(Sea_path)
AVG_LA_Data = AQ_Values_AVG(LA_path)

AVG_SEA_Data.to_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code/Datasets/USA/LASEA/SEA_AVG_AQ_VALS.csv', index = False)
AVG_LA_Data.to_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code/Datasets/USA/LASEA/LA_AVG_AQ_VALS.csv', index = False)
