import pandas as pd 
import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/COVID/CC_COVID/Confirmed_Cases_CC.csv')
County_data = pd.DataFrame()
County_data['State'] = df['Province_State']
County_data['County'] = df['Admin2']
County_data['Lat'] = df['Lat']
County_data['Long'] = df['Long_']
#print(list(County_data.State=='Hawaii'))

County_data = County_data[County_data.State!='Hawaii']

gdf = gpd.GeoDataFrame(County_data, geometry=gpd.points_from_xy(County_data.Long, County_data.Lat))
USA = gpd.read_file('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Maps/cb_2018_us_state_500k/cb_2018_us_state_500k.shp')
USA = USA.drop(index = [13,27,37,38,44,45])
USA = USA.drop(index = [42])

ax = USA.plot(color='white', edgecolor='grey')
gdf.plot(ax=ax, color='black', markersize=2)
ax.set_xlabel('Longitude', fontsize=24)
ax.set_ylabel('Latitude', fontsize=24)
plt.title('Counties Represented in Analysis', fontsize=24)
plt.show()
