import sys
import MapReduce

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, 1)

# Part 3
def reducer(key, list_of_values):
    # key: word    
    mr.emit((key, len(list_of_values)))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
