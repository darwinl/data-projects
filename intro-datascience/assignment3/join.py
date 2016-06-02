import sys
import MapReduce

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    order_id = record[1]
    value = record
    mr.emit_intermediate(order_id, value)

# Part 3
def reducer(key, list_of_records):
    # key: word
    
    line_items = []
    for record in list_of_records:
      if record[0] == 'order':
        order_record = record
      if record[0] == 'line_item':
        line_items.append(record)
    
    for line_item in line_items:
       mr.emit((order_record + line_item))
                

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
