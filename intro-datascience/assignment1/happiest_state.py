import sys
import json

def hw(sent_file,tweet_file):
    #print 'Hello, world!'
    scores = create_sentiment_dict(sent_file)
    calculate_happy_states(tweet_file, scores)        

def lines(fp):
    print str(len(fp.readlines()))

def create_sentiment_dict(sent_file):
    scores = {}
    for line in sent_file:
        term,score = line.split("\t")
        scores[term] = int(score)
        
    return scores

def update_state_sentiment(line, scores, states):
    response = json.loads(line)
    sentiment = 0
    #print response['text']
    
    if ( 'place' in response and response['place'] != None ): 
        if (response['place']['country_code'] == 'US'):
            if response['place']['full_name'].split(", ")[1] in states:

                for word in response['text'].split():
                    if word in scores: 
                        sentiment += scores[word]
                        
                state = response['place']['full_name'].split(", ")[1]
                
                #print "before:", state, states[state], sentiment
                
                states[state] = states[state] + sentiment   
                
                #print "after:", state, states[state]   
    
    return sentiment
        
def calculate_happy_states(tweet_file, scores):

    states = {'AL':0,'AK':0, 'AZ':0, 'AR':0, 'CA':0, 'CO':0, 
                'CT':0, 'DE':0, 'DC':0, 'FL':0, 'GA':0, 'HI':0, 
                'ID':0, 'IL':0, 'IN':0, 'IA':0, 'KS':0, 'KY':0,
                'LA':0, 'ME':0, 'MD':0, 'MA':0, 'MI':0, 'MN':0,
                'MS':0, 'MO':0, 'MT':0, 'NE':0, 'NV':0, 'NH':0,
                'NJ':0, 'NM':0, 'NY':0, 'NC':0, 'ND':0, 'OH':0,
                'OK':0, 'OR':0, 'PA':0, 'RI':0, 'SC':0, 'SD':0, 
                'TN':0, 'TX':0, 'UT':0, 'VT':0, 'VA':0, 'WA':0, 
                'WV':0, 'WI':0, 'WY':0}
                
    for line in tweet_file:            
        update_state_sentiment(line, scores, states)
        
    happiest_state = "AL"
    happiest_score = 0
    for state in states.keys():
        if states[state] > happiest_score:
            happiest_state = state
            
    print happiest_state        
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    hw(sent_file,tweet_file)
    
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
