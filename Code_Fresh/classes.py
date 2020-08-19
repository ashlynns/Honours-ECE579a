import pandas as pd 
import numpy as np

features = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Features_v1.csv')
features['Class'] = " "

features_C1 = features[features['Good Days']>0.90]
features_C1['Class'] = np.ones(len(features_C1))*1

features_C2 = features[(features['Good Days']<0.90) & (features['Good Days']>0.835)]
features_C2['Class'] = (np.ones(len(features_C2)))*2

features_C3 = features[(features['Good Days']<0.835) & (features['Good Days']>0.75)]
features_C3['Class'] = (np.ones(len(features_C3)))*3

features_C4 = features[features['Good Days']<0.75]
features_C4['Class'] = (np.ones(len(features_C4)))*4

step = [features_C1, features_C2, features_C3, features_C4]
features_classified = pd.concat(step)
features_classified = features_classified.sort_index()

features_classified.to_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Features_classified.csv')