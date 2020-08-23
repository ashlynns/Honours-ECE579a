import pandas as pd 

AQI_Features = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/AQI_Features.csv')
Covid_Cases_Det_Classes = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/COVID/Case_Curve_Class_D.csv')
Covid_Cases_Spectral = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Spectral_Clustering_Classes.csv')
Cases_and_Deaths = pd.read_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Normalized_Cases_Deaths.csv')

Features = AQI_Features
Features['Norm_Cases'] = Cases_and_Deaths.Cases
Features['Norm_Deaths'] = Cases_and_Deaths.Deaths
Features['Case_Det_Class'] = Covid_Cases_Det_Classes.Case_Curve_Class 
Features['Case_Spectral_Class'] = Covid_Cases_Spectral.SpectralClass


Features.to_csv('/Users/Ashlynn/Desktop/Summer 2020/Honours-ECE579a/Code_Fresh/Datasets/Features.csv', index=False)
