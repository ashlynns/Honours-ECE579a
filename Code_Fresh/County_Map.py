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

gdf = gpd.GeoDataFrame(County_data, geometry=gpd.points_from_xy(County_data.Long, County_data.Lat))
USA = gpd.read_file('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Maps/cb_2018_us_state_500k/cb_2018_us_state_500k.shp')
USA = USA.drop(index = [13,27,37,38,44,45])

ax = USA.plot(color='white', edgecolor='black')
gdf.plot(ax=ax, color='red', markersize=1)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
plt.title('Counties Represented in Analysis')
plt.show()
