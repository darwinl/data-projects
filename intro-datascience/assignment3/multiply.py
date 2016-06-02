import sys
import MapReduce

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    ## handle matrix A
    
    if record[0] == 'a':
        for i in range(5):
            mr.emit_intermediate((record[1], i), record)
    else:
        for i in range(5):
            mr.emit_intermediate((i,record[2]), record)      

# Part 3
def reducer(key, list_of_values):
    # key: word
    ## create the a array
    a = {}
    b = {}
    #print key, list_of_values
    for v in list_of_values:
        if v[0] == 'a':
            a[v[2]] = v[3]
        if v[0] == 'b':
            b[v[1]] = v[3]
    
    cell = 0        
    for k,v in a.items():
        if k in b:
            cell += v * b[k]
        
    mr.emit((key[0], key[1], cell))
                
            


# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
