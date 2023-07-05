# Punyaja Mishra
# 0660001
# Assignment 4: Data Wrangling Techniques


import sklearn as sk
from sklearn import preprocessing
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# kaggle data and then converting to dataframe (source 1)
kaggle_data = pd.read_csv('kaggle.csv')

# world population review data and then converting to dataframe (source 2)
worldreview_data = pd.read_csv('worldreview.csv')


# merging the data based on the same column both of them have - country
df = pd.merge(left=kaggle_data, right=worldreview_data, left_on='country', right_on='country')

# ensuring and removing the missing values (NaN)
mergedata = df.dropna()

# selecting a part of data 
# TRANSFORMING THE DATA
# CLUSTERING - KMeans
data = mergedata.iloc[0:100,1:2]
kmeans = KMeans(n_clusters=4, max_iter=300)
kmeans.fit(data.values)
predictions = kmeans.predict(mergedata.iloc[100:,1:2])

#plotting the data
plt.scatter(data.iloc[:,1], data.iloc[:,2], c=predictions)
plt.title("Data k-means, Clusters=4")
plt.show()











