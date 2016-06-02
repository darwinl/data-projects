import csv as csv
import numpy as np

test_file_object = csv.reader(open('test.csv', 'rb')) 
header = test_file_object.next()  #The next() command just skips the 
                                 #first line which is a header
                                 
open_file_object = csv.writer(open("genderbasedmodelpy.csv", "wb"))

# write the header
open_file_object.writerow(['PassengerId','Survived'])

for row in test_file_object:       #for each row in test.csv
    if row[3] == 'female':             #is it a female, if yes then
        open_file_object.writerow([row[0],1]) #and write the row to the
    else:                              #new file else
        open_file_object.writerow([row[0],0]) #survive (0) and write row 