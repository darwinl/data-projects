import sys
import MapReduce

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)

# Part 3
def reducer(key, list_of_values):
    # key: word
    unique_list = list(set(list_of_values))
    mr.emit((key, unique_list))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
