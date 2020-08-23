import pandas as pd 

# Importing list of counties in analysis
CS_List = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/AQI/Combined_AQI.csv')
CS_List = list(CS_List['County']+CS_List['State'])
print(len(CS_List))

######## FEATURES EXTRACTED FROM POPULATION DATA FILE ############
# Importing population data file 
RS_Headers = ['STATE','STNAME', 'CTYNAME', 'YEAR', 'AGEGRP', 'TOT_POP', 'BA_MALE', 'BA_FEMALE', 'H_MALE', 'H_FEMALE']
population_RSo = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Confounding/cc-est2019-alldata copy.csv', encoding = 'cp1252', usecols = RS_Headers)
ctyname = []
# Filtering city names to match existing list 
t = (list(population_RSo['CTYNAME']))
for i in range(len(t)):
	if (t[i].rsplit(' ', 1)[1] == 'City'):
		ctyname.append(t[i])
	elif (t[i].rsplit(' ', 1)[1] == 'city'):
		x = t[i].rsplit(' ', 1)[0]+' City'
		ctyname.append(x)
	else:
		ctyname.append(t[i].rsplit(' ', 1)[0])
population_RSo['CTYNAME']=ctyname
CS = population_RSo['CTYNAME']+population_RSo['STNAME']

# Keeping only the counties that are represented in analysis
population_RSo.insert(3, 'CS', CS)
population_RSo_CC = population_RSo[population_RSo['CS'].isin(CS_List)]

# Gathering Racial data
population_RS = population_RSo_CC[(population_RSo_CC['YEAR']==12) & (population_RSo_CC['AGEGRP']==0)]
H_pct = ((population_RS['H_MALE']+population_RS['H_FEMALE'])/population_RS['TOT_POP'])*100
population_RS.insert(7,'HISPANIC_PCT', H_pct)
B_pct = ((population_RS['BA_MALE']+population_RS['BA_FEMALE'])/population_RS['TOT_POP'])*100
population_RS.insert(7,'BLACK_PCT',B_pct)
population_RS = population_RS.drop(['YEAR','H_MALE','H_FEMALE','BA_MALE','BA_FEMALE','AGEGRP'], axis=1)

# Creating DF for confounding variables 
Confounding = population_RS

# Generating the percentage of ppl per county over 70yo
over70 = population_RSo_CC[(population_RSo_CC['YEAR']==12) & ((population_RSo_CC['AGEGRP']>=15)|(population_RSo['AGEGRP']==0))]
over70 = over70.drop(['YEAR','H_MALE','H_FEMALE','BA_MALE','BA_FEMALE'], axis=1)
over70_pct = []
i=0
while i<len(over70):
	abv = over70['TOT_POP'].iloc[i+1]+ over70['TOT_POP'].iloc[i+2]+ over70['TOT_POP'].iloc[i+3]+over70['TOT_POP'].iloc[i+4]
	pct = (abv/over70['TOT_POP'].iloc[i])*100
	over70_pct.append(pct)
	i+=5

Confounding.insert(7,'OVER_70_PCT', over70_pct)

############## LAND MASS DATASET ##################

Land_Mass = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Confounding/LandData.csv')

# Removing State Acronyms
county = []
t = (list(Land_Mass['County']))
for i in range(len(t)):
	x = t[i].rsplit(',', 1)[0]
	county.append(x)

# Keeping only the counties within analysis
Land_Mass['County'] = county
CS = Land_Mass['County']+Land_Mass['State']
Land_Mass.insert(2,'CS',CS)
Land_Mass_CC = Land_Mass[Land_Mass['CS'].isin(CS_List)]

# Merging land mass with data
LA = list(Land_Mass_CC['Land Area'])
Confounding.insert(7, 'Land_Mass', LA)

# Dividing population by land mass to get population density
PD = Confounding['TOT_POP']/Confounding['Land_Mass']
Confounding.insert(5,'POP_DENSITY', PD)
Confounding = Confounding.drop('Land_Mass', axis=1)

############# HEALTH INSURANCE DATASET #################
HI = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Confounding/Health_Insurance1.csv', encoding = 'cp1252')

# Removing State Acronyms
countyL = []
state = []
t = (list(HI['LOC']))
for i in range(len(t)):
	x = t[i].rsplit(', ', 1)
	state.append(x[1])
	county = x[0]
	xc = county.rsplit(' ',1)
	if xc[1] == 'city':
		countyL.append(xc[0]+' City')
	else: 
		countyL.append(xc[0])

HI.insert(1,'County', countyL)
HI.insert(2, 'State', state)
CS = HI['County']+HI['State']
HI.insert(3,'CS', CS)
HI = HI[HI['CS'].isin(CS_List)]

healthI = list(HI['PCT_HI'])
Confounding.insert(9, 'HLTH_INS_PCT', healthI)

############# INCOME DATASET #################
INC = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Confounding/Income.csv', encoding = 'cp1252')

countyL = []
state = []
t = (list(INC['LOC']))
for i in range(len(t)):
	x = t[i].rsplit(', ', 1)
	state.append(x[1])
	county = x[0]
	xc = county.rsplit(' ',1)
	if xc[1] == 'city':
		countyL.append(xc[0]+' City')
	else: 
		countyL.append(xc[0])

INC.insert(1,'County', countyL)
INC.insert(2, 'State', state)
CS = INC['County']+INC['State']
INC.insert(3,'CS', CS)
INC = INC[INC['CS'].isin(CS_List)]

MEAN_INC = list(INC['Mean Income'])
MED_INC = list(INC['Median Income'])

Confounding.insert(10, 'MEAN_INCOME', MEAN_INC)
Confounding.insert(11, 'MEDIAN_INCOME', MED_INC)

################## POVERTY DATASET ##################
POV = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Confounding/Poverty.csv', encoding = 'cp1252')

countyL = []
state = []
t = (list(POV['LOC']))
for i in range(len(t)):
	x = t[i].rsplit(', ', 1)
	state.append(x[1])
	county = x[0]
	xc = county.rsplit(' ',1)
	if xc[1] == 'city':
		countyL.append(xc[0]+' City')
	else: 
		countyL.append(xc[0])

POV.insert(1,'County', countyL)
POV.insert(2, 'State', state)
CS = POV['County']+POV['State']
POV.insert(3,'CS', CS)
POV = POV[POV['CS'].isin(CS_List)]

PCT_POV = list(POV['PCT_IN_POVERTY'])
Confounding.insert(12, 'PCT_POVERTY', PCT_POV)


Confounding = Confounding.drop('STATE', axis=1)
#Confounding.to_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Confounding/Confounding_Dataset.csv', index=False)


