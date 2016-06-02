import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def hashtag_count(hashtag):
    return hashtag[1]
    
def main():
    tweet_file = open(sys.argv[1])
    
    hashtag_dict = {}
    
    for line in tweet_file:
        response = json.loads(line)
        if 'entities' in response:
            if ( 'hashtags' in response['entities'] ):        
                #print response['text'], response['entities']['hashtags']
                for hashtag in response['entities']['hashtags']:
                    if hashtag['text'] in hashtag_dict:
                        hashtag_dict[hashtag['text']] =  hashtag_dict[hashtag['text']] + 1               
                    else:
                        hashtag_dict[hashtag['text']] = 1

    hashtags = hashtag_dict.items()
    sorted_hashtags = sorted(hashtags, key=hashtag_count, reverse=True)
    
    for i in range(10):
        print sorted_hashtags[i][0], float(sorted_hashtags[i][1])
    
if __name__ == '__main__':
    main()