# Punyaja Mishra
# 0660001
# Lab 8 : Decision Trees & K-Nearest Neighbour

#Observation -
# Part 2 :
# Part 3 :

import sklearn.datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

#loading iris data; X is data; y is target variable; splitting data from the start
X,y = sklearn.datasets.load_iris(return_X_y=True)
# 1/3 data for testing; 2/3 for training
X_trainingData, X_testData, y_trainingData, y_testData = train_test_split(X,y,test_size=0.33)

########## Part 2: Decision Trees
myClassifier = DecisionTreeClassifier()
#get labels of training data
myClassifier.fit(X_trainingData, y_trainingData)
# prediction of labels of test data
prediction = myClassifier.predict(X_testData)

print("Punyaja Mishra 0660001\n")
print("\nPart 2: Decision Tree Classifier\n\n")
print("Classification Report\n")
print(classification_report(y_testData, prediction))
print("Confusion Matrix\n")
print(confusion_matrix(y_testData, prediction))

######### Part 3: KNN
# using 3 neighbours and unweighted distances
# Output the classification report and confusion matrix and submit a screenshot of the result (1 mark)

#initilaize the model:
knn = KNeighborsClassifier(n_neighbors=3)

#cross_validation: myScores is the result of how good the model is
myScores = cross_val_score(knn, X,y, scoring='accuracy', cv=KFold(n_splits=10))
knn.fit(X_trainingData, y_trainingData)
# prediction of labels of test data
prediction1 = knn.predict(X_testData)

print("Punyaja Mishra 0660001\n")
print("\nPart 3: K Nearest Neighbor\n\n")
print("Classification Report\n")
print(classification_report(y_testData, prediction1))    
print("Confusion Matrix\n")
print(confusion_matrix(y_testData, prediction1))
