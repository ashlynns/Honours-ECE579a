import pandas as pd 
import numpy as np

Feature_in_path = '/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Features_v1.csv'
Features = pd.read_csv(Feature_in_path)
Feature_out_path = '/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Features/Pre_Norm/'

Features_max_HAZ = Features[Features['Hazardous Days']!=0]
Features_max_HAZ['Class']= 5*np.ones(len(Features_max_HAZ.index))
#Features_max_HAZ.to_csv(Feature_out_path+'Features_max_HAZ.csv', index=False)
Features = Features.drop(index =Features_max_HAZ.index)

Features_max_VUH = Features[Features['Very Unhealthy Days']!=0]
Features_max_VUH['Class']=4*np.ones(len(Features_max_VUH.index))
#Features_max_VUH.to_csv(Feature_out_path+'Features_max_VUH.csv', index=False)
Features = Features.drop(index =Features_max_VUH.index)

Features_max_UH = Features[Features['Unhealthy Days']!=0]
Features_max_UH['Class']=3*np.ones(len(Features_max_UH.index))
#Features_max_UH.to_csv(Feature_out_path+'Features_max_UH.csv', index=False)
Features = Features.drop(index =Features_max_UH.index)

Features_max_UHS = Features[Features['Unhealthy for Sensitive Groups Days']!=0]
Features_max_UHS['Class']=2*np.ones(len(Features_max_UHS.index))
#Features_max_UHS.to_csv(Feature_out_path+'Features_max_UHS.csv', index=False)
Features = Features.drop(index =Features_max_UHS.index)

Features_max_MOD = Features[Features['Moderate Days']!=0]
Features_max_MOD['Class'] = 1*np.ones(len(Features_max_MOD.index))
#Features_max_MOD.to_csv(Feature_out_path+'Features_max_MOD.csv', index=False)
#Features = Features.drop(index =Features_max_MOD.index)

test = [Features_max_MOD, Features_max_UHS, Features_max_UH,Features_max_VUH, Features_max_HAZ ]
Class_DF = pd.concat(test)
Class_DF = Class_DF.sort_index()

Class_DF.to_csv(Feature_out_path+'Features_Class_Labels.csv', index = False)

#print(Features_max_UHS)
#print(Class_DF)