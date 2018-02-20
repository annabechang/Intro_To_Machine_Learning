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


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score

features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]     

clf = svm.SVC(kernel="rbf", C=1000.0)
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

print pred[10]
print pred[26]
print pred[50]




"""
from sklearn.svm import SVC
cclf = SVC(C=10000.0, kernel='rbf')
features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 
clf.fit(features_train, labels_train)
print(clf.score(features_test,labels_test)) """

#########################################################


"""(py27) MacBook-Air-2:svm Anna$ python svm_author_id_slice_rbf.py
/Users/Anna/anaconda/envs/py27/lib/python2.7/site-packages/sklearn/cross_validation.py:41: DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved. Also note that the interface of the new CV iterators are different from that of this module. This module will be removed in 0.20.
  "This module will be removed in 0.20.", DeprecationWarning)
no. of Chris training emails: 7936
no. of Sara training emails: 7884
0.616040955631"""
