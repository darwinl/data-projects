import sys
import json

def create_term_frequency_dict(tweet_file):

    terms = {}
    for line in tweet_file:
        response = json.loads(line)
        for word in response['text'].split():
            if word in terms:
                terms[word] = terms[word] + 1
            else:
                terms[word] = 1
    return terms            
            
def calculate_frequency(terms):

    total_term_count = 0
    for key in terms.keys():
        total_term_count += terms[key]
        
    #print "total term count is %d" % (total_term_count)
        
    for key in terms.keys():
        print "%s %f" % (key,float(terms[key])/total_term_count)


def hw(tweet_file):
    #print 'Hello, world!'
    
    ## first create dictionary for term:termcount
    terms = create_term_frequency_dict(tweet_file)
    calculate_frequency(terms)

def main():
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    
    hw(tweet_file)
    
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
