import csv as csv
import numpy as np

csv_file_object = csv.reader(open('train.csv', 'rb')) 
header = csv_file_object.next()  #The next() command just skips the 
                                 #first line which is a header
                                 
data=[]
for row in csv_file_object:      #Run through each row in the csv file
    data.append(row)


data = np.array(data) 	         #Then convert from a list to an array
			         #Be aware that each item is currently
                                 #a string in this format 
                                 

#The size function counts how many elements are in
#in the array and sum (as you would expects) sums up
#the elements in the array.

number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
proportion_survivors = number_survived / number_passengers

print "Proportion survivors", proportion_survivors

# find all the females/mailes

women_only_stats = data[0::,4] == "female" #This finds where all 
men_only_stats = data[0::,4] != "female"   

print "women only"
print women_only_stats

print "men only"
print men_only_stats

#Using the index from above we select the females and males separately
women_onboard = data[women_only_stats,1].astype(np.float)     
men_onboard = data[men_only_stats,1].astype(np.float)

print women_onboard
print men_onboard

# Then we find the proportions of them that survived
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)  
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard) 

#and then print it out
print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived                                           