import sys
import json
import re

def hw(sent_file,tweet_file):
    #print 'Hello, world!'
    scores = create_sentiment_dict(sent_file)
    calculate_sentiments(tweet_file, scores)        

def lines(fp):
    print str(len(fp.readlines()))

def create_sentiment_dict(sent_file):
    scores = {}
    for line in sent_file:
        term,score = line.split("\t")
        scores[term] = score
        
    return scores

def calculate_sentiment(line, scores):
    response = json.loads(line)
    sentiment = 0
    for word in response['text'].split():
        if word.lower() in scores: 
            sentiment += int(scores[word])
            
    return sentiment
        
def calculate_sentiments(tweet_file, scores):
    
    for line in tweet_file:
        line_score = calculate_sentiment(line, scores)
        response = json.loads(line)
        
        for word in response['text'].split():
                if word.lower() not in scores:
                    print word, " ", "%f" % (line_score)            

        
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    hw(sent_file,tweet_file)
    
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
