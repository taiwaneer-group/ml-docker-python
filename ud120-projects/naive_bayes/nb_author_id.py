#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

### import sklearn modules
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

# Initial GaussianNB
clf = GaussianNB()

# Set the timer and calculate the training time
t0 = time()
# Fit the training data
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0,3), "s"

# Set the timer and calculate the predicting time
t0 = time()
# Get the prediction based on the training data
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0,3), "s"

# Get the accuracy for the prediction
print accuracy_score(pred, labels_test)




#########################################################


