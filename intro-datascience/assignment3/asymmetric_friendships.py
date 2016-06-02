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
    mr.emit_intermediate("".join(sorted([person,friend])), [person,friend])

# Part 3
def reducer(key, list_of_values):
    # key: word
    if len(list_of_values) == 1:
        person = list_of_values[0][0]
        friend = list_of_values[0][1]
        mr.emit((person,friend))
        mr.emit((friend,person))


# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
