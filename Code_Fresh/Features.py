import pandas as pd 

AQI = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/AQI/Combined_AQI.csv')
CC_Cases = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/COVID/CC_COVID/Confirmed_Cases_CC.csv')
CC_Deaths = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/COVID/CC_COVID/Deaths_CC.csv')
CaseRate = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Cases_Slopes.csv')

Features = AQI 

# List of all the counties in the feature space 
County_State_Features = Features['County']+', '+Features['State']
# Getting cencus population data for the counties in the feature space 
populations = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Confounding/County_population_reduced.csv', encoding = 'Windows 1252')
populations = populations[populations['CountyState'].isin(County_State_Features)]
populations = populations.reset_index(drop=True)

# Obtain the highest number of cases from a county
Case_Values = CC_Cases.iloc[:, 12:len(CC_Cases.columns)]
Max_Cases = Case_Values.max(axis=1)

Max_Rate = CaseRate.max(axis=1)

# Obtain the highest number of deaths from a county
Death_Values = CC_Deaths.iloc[:, 12:len(CC_Deaths.columns)]
Max_Deaths = Death_Values.max(axis=1)


# Dividing the number of deaths and cases in a county by their population
#Features['Population'] = populations['Projected Population']
Features['COVID Deaths (Normalized by Population)'] = Max_Deaths/populations['Projected Population']
Features['COVID Cases (Normalized by Population)'] = Max_Cases/populations['Projected Population']
Features['COVID Cases Rates'] = Max_Rate

# Exporting Features
populations.to_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Confounding/CC_populations.csv', index=False)
Features.to_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Features_v1.csv', index = False)