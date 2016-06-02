import sys
import MapReduce

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    sequence_id = record[0]
    nuc = record[1]
    trimmed_nuc = nuc[0:len(nuc)-10]
    mr.emit_intermediate(trimmed_nuc,1)

# Part 3
def reducer(key, list_of_values):
    # key: word
    mr.emit(key)


# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
