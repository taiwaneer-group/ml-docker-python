#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
### C value the bigger the better accuracy
clf = SVC(C=10000.0, kernel="rbf")

### Set smaller dataset for training data
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

### Set the timer and calculate the training time
t0 = time()
### Fit the training data
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0,3), "s"

### Set the timer and calculate the predicting time
t1 = time()
### Set the prediction based on the training data
pred = clf.predict(features_test)
print "predicting time:", round(time()-t1,3), "s"

# Accuracy
print accuracy_score(pred, labels_test)

# Prediction for element 10, 26 and 50
print ("element 10:", pred[10])
print ("element 26:", pred[26])
print ("element 50:", pred[50])

# Print total lengh of the test events
print len(pred)

# Total predcition for Chris's email
chrisEmailCount = 0
for x in pred:
    if x == 1:
        chrisEmailCount += 1

print chrisEmailCount
#########################################################


