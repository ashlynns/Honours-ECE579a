import pandas as pd 
from datetime import date
import numpy as np
import matplotlib.pyplot as plt

MTL_AQ = pd.read_csv('../Datasets/Canada/montreal-air-quality.csv', index_col = 0)
TO_AQ = pd.read_csv('../Datasets/Canada/toronto-dt-air-quality.csv')


MTL_AQ_values = MTL_AQ.max(axis=1)
TO_AQ_values = TO_AQ.max(axis=0)

print(MTL_AQ[' pm25'])
print(MTL_AQ_values)


