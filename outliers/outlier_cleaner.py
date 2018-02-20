#!/usr/bin/python

'''
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    for pred, a, net_w in zip(predictions, ages, net_worths):
        cleaned_data.append((a[0], net_w[0], pred[0] - net_w[0]))

    cleaned_data.sort(key=lambda i: i[2]) # Sort the data by the 2nd index (third element, which is the error)

    return cleaned_data[:81] # returns the first 81 elements (or 90% of the original length)
'''
def outlierCleaner(predictions, ages, net_worths):
   
    cleaned_data = []

    for (prednw, actualnw, age) in zip(predictions, net_worths, ages):
        cleaned_data.append((age[0], actualnw[0], prednw[0] - actualnw[0]))

    # sort list based on error
    cleaned_data.sort(cd, key = lambda x: x[2])

    return cleaned_data[:81]

    '''
def outlierCleaner(predictions, ages, net_worths):
 import numpy as np
 cleaned_data = np.concatenate((predictions, ages, net_worths, abs(net_worths-predictions)), axis = 1)
 cleaned_data = cleaned_data[np.argsort(cleaned_data[:,3])]
 return cleaned_data[:int(len(cleaned_data)*.9),1:]


'''
