import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    
    for line in tweet_file:
        response = json.loads(line)
        if 'entities' in response:
            if ( 'hashtags' in response['entities'] and len(response['entities']['hashtags']) > 0 ):        
                print response['text'], response['entities']['hashtags']
                for hashtag in response['entities']['hashtags']:
                    print hashtag['text']

        #break                
        #if ( 'coordinates' in response and response['coordinates'] != None ): print 'coordinates:', response['coordinates']
        #if 'user' in response: 
            #print 'user', response['user']
            #print type(response['user'])
            #print response['user'].keys()
            #print response['user']['created_at']
        

if __name__ == '__main__':
    main()