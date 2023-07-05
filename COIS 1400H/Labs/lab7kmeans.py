# Punyaja Mishra
# 066001
# Lab 7 : K-means Clustering for Number of Clsuters = 2 & 3

import sklearn.datasets
from sklearn import preprocessing
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# load the data
# we are loadign the iris data from the sklearn datasets & lso standardizing the data
data= sklearn.datasets.load_iris()
numData = data['data']
scaledData = preprocessing.scale(numData)

# K- Means

######## CLUSTERS =2
# we are using the funciton kmeans from skelarn to apply kmeans clustering on the iris dtata
kmeans = KMeans(n_clusters=2, max_iter=300)
kmeans.fit(scaledData)
# the predicitons of the closest cluster for each sample in our iris data - which cluster it belongs to
predictions = kmeans.predict(scaledData)
print(kmeans.cluster_centers_)

# plotting predicted labels as a scatter
plt.scatter(scaledData[:,0], scaledData[:,1],c=predictions)
plt.title("Iris Data k-means, Cluster=2")
plt.show()

                         
######## CLUSTERS =3
# we are using the funciton kmeans from skelarn to apply kmeans clustering on the iris dtata
kmeans1 = KMeans(n_clusters=3, max_iter=300)
kmeans1.fit(scaledData)
# the predicitons of the closest cluster for each sample in our iris data - which cluster it belongs to
predictions1 = kmeans1.predict(scaledData)
print(kmeans1.cluster_centers_)

# plotting predicted labels as a scatter
plt.scatter(scaledData[:,0], scaledData[:,1],c=predictions1)
plt.title("Iris Data k-means, Cluster=3")
plt.show()
