# Import the random forest package
import csv as csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier 

csv_file_object = csv.reader(open('train.csv', 'rb')) 
header = csv_file_object.next()  #The next() command just skips the 
                                 #first line which is a header
                                 
train_data=[]
for row in csv_file_object:      #Run through each row in the csv file
    if row[4] == "female":
       row[4] = 0
    else:
       row[4] = 1
    
    cabin = {'C':0,'S':1,'Q':2}
    if row[11] not in cabin:
       row[11] = 'C'
    
    row = row[1:3] + row[4:8] + [row[9],cabin[row[11]]]
    train_data.append(row)


train_data = np.array(train_data) 	         #Then convert from a list to an array
			         #Be aware that each item is currently
                                 #a string in this format 

#print train_data[::].astype(np.float)
print train_data

train_data = np.array(train_data, dtype='|S4')
train_data = train_data.astype(np.float)


# Create the random forest object which will include all the parameters
# for the fit
Forest = RandomForestClassifier(n_estimators = 100)

# Fit the training data to the training output and create the decision
# trees
Forest = Forest.fit(train_data[0::,1::],train_data[0::,0])

# Take the same decision trees and run on the test data
#Output = Forest.predict(test_data)