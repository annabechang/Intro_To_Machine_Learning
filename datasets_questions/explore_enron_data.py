#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#first look of the dataset 
#print enron_data

#How many data points (people) are in the dataset?
print "Number of people %d"%len(enron_data.keys())

#For each person, how many features are available?
print("number of features", len(enron_data["CAUSEY RICHARD A"].keys()))

#The poi feature records whether the person is a person of interest, according to our definition. How many POIs are there in the E+F dataset?
"""
count = 0
for n in enron_data.keys():
      
      if n['poi'] == True:
            count +=1 
print ("count",count)

print sum(enron_data.ix['poi'])

"""

print "number of poi %d" %sum(x['poi'] for x in enron_data.values())



"""
poi_email = open('../final_project/poi_names.txt').read().split("\,")


print("Poi occurs is: ", poi_email.count("(y)")) 

poi = 0
for w in poi_email:
      if w == "(y)":
            poi +=1
print poi

poi_txt = open('../final_project/poi_names.txt').readlines()
print poi_txt
pois = [txt.strip() for txt in poi_txt]
print len(pois) - 2
"""
# number of pois in name txt
count = 0
poi_names = open("../final_project/poi_names.txt").read().split()
for name in poi_names:
      if "(y)" in name or "(n)" in name:
            count = count + 1
print("Poi in names is",count)

# total stock value for James
print(enron_data["PRENTICE JAMES"]['total_stock_value'])


print(enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])

print(enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])

print(enron_data["FASTOW ANDREW S"]['total_payments'])
print(enron_data["SKILLING JEFFREY K"]['total_payments'])
print(enron_data["LAY KENNETH L"]['total_payments'])

#Quantified salary


print "number of salary %d" %sum([1 for x in enron_data.values() if x['salary'] != 'NaN'])

print "number of emails %d" %sum([1 for x in enron_data.values() if x['email_address'] != 'NaN'])

print "number of nan for total payment %d" %sum([1 for x in enron_data.values() if x['total_payments'] == 'NaN'])

print "number of nan for pois %d" %sum([1 for x in enron_data.values() if (x['total_payments'] == 'NaN' and x['poi'] == True)])



