# For linear algebra
import numpy as np
# For data processing
import pandas as pd

#Load the data set
df = pd.read_csv('C:\\Users\\Ithur\\Documents\\GitHub\\Project22\\Application\\resource\\dataset.csv')
#Display the shape of the data set
print('Size of datae is :',df.shape)
#Display data
print(df[0:5])