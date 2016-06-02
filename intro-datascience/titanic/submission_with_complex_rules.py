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
                                 


fare_ceiling = 40
data[data[0::,9].astype(np.float) >= fare_ceiling, 9] = fare_ceiling-1.0
fare_bracket_size = 10
number_of_price_brackets = fare_ceiling / fare_bracket_size
number_of_classes = 3 #There were 1st, 2nd and 3rd classes on board 
# Define the survival table
survival_table = np.zeros((2, number_of_classes, number_of_price_brackets))

for i in xrange(number_of_classes):       #search through each class
  for j in xrange(number_of_price_brackets):   #search through each price

    women_only_stats = data[                          
                         (data[0::,4] == "female")    
                       &(data[0::,2].astype(np.float) 
                             == i+1)                                       
                       &(data[0:,9].astype(np.float)  
                            >= j*fare_bracket_size)   
                       &(data[0:,9].astype(np.float)  
                            < (j+1)*fare_bracket_size)
                          , 1]                        

    men_only_stats = data[                            
                         (data[0::,4] != "female")    
                       &(data[0::,2].astype(np.float) 
                             == i+1)                  
                       &(data[0:,9].astype(np.float)  
                            >= j*fare_bracket_size)   
                       &(data[0:,9].astype(np.float)  
                            < (j+1)*fare_bracket_size)
                          , 1] 
    survival_table[0,i,j] = np.mean(women_only_stats.astype(np.float)) #Women stats
    survival_table[1,i,j] = np.mean(men_only_stats.astype(np.float)) #Men stats 
    
survival_table[ survival_table != survival_table ] = 0

survival_table[ survival_table < 0.5 ] = 0
survival_table[ survival_table >= 0.5 ] = 1     

test_file_obect = csv.reader(open('test.csv', 'rb'))
fname = "genderclasspricebasedmodelpy.csv"
open_file_object = csv.writer(open(fname, "wb"))
header = test_file_obect.next()  

# write the header
open_file_object.writerow(['PassengerId','Survived'])

for row in test_file_obect:                   #we are going to loop
                                              #through each passenger
                                              #in the test set                     
  for j in xrange(number_of_price_brackets):  #For each passenger we
                                              #loop thro each price bin
    try:                                      #Some passengers have no
                                              #price data so try to make
      row[8] = float(row[8])                  # a float
    except:                                   #If fails: no data, so 
      bin_fare = 3-float(row[1])              #bin the fare according class
      break
                                         #Break from the bin loop
    if row[8] > fare_ceiling:              #If there is data see if
                                              #it is greater than fare
                                              #ceiling we set earlier
      bin_fare = number_of_price_brackets-1   #If so set to highest bin
      break                                   #And then break bin loop
    if row[8] >= j*fare_bracket_size and row[8] < (j+1)*fare_bracket_size:  
      bin_fare = j                            #then assign index
      break  
      
  print "Bin fare class for row passenger id ", row[0], row[8], bin_fare
      
  if row[3] == 'female': 
    survived_value = int(survival_table[0,float(row[1])-1,bin_fare])
    open_file_object.writerow([row[0],survived_value])                 #And write out row          
  else:
    survived_value = int(survival_table[1,float(row[1])-1,bin_fare])
    open_file_object.writerow([row[0],survived_value])              
