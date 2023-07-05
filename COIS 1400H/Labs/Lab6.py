# Punyaja Mishra
# 0660001
# Lab 6 : Visualizations using Matplotlib 



            ### Part 1 Setup: done using command line
import matplotlib.pyplot as plt
import numpy as np
from pydataset import data


            ### Part 2 Loading data & creating a first plot
iris = data('iris')

#scatter plot
plt.subplot(221)#subplot 1
plt.scatter(iris.iloc[:,0], iris.iloc[:,1], s=80, marker='*',c=iris.iloc[:,2])
plt.title("Punyaja Mishra #066001 | Iris Scatter Plot 1")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
cbar= plt.colorbar()
cbar.set_label("elevation (m)", labelpad=+1)


            ### Part 3 Exploring plotting options for the iris data

#pie chart
plt.subplot(222) #subplot 2
iris['Species'].value_counts().plot.pie(shadow=True,figsize=(10,8))
plt.title('Punyaja Mishra #066001 | Iris Pie Chart')


#Histogram
plt.subplot(223) #subplot 3
plt.hist(iris.iloc[:,0], bins = 20, color = "blue")
plt.title("Punyaja Mishra #066001 | Iris Histogram")
plt.xlabel("Sepal Length")
plt.ylabel("Count")


            ### Part 4 Creating 4 subplots to get final output
#scatter plot
plt.subplot(224) #subplot 4
plt.scatter(iris.iloc[:,2], iris.iloc[:,3], s=80, marker='*',c=iris.iloc[:,0])
plt.title("Punyaja Mishra #066001 | Iris Scatter Plot 2")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
cbar= plt.colorbar()
cbar.set_label("elevation (m)", labelpad=+1)


#setting title, and padding for the subplot box & plt.show()
plt.tight_layout(pad=5.0)
plt.suptitle('Punyaja Mishra #0660001')
plt.show()
