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
        if ( 'place' in response and response['place'] != None ): 
            if (response['place']['country_code'] == 'US'):
                print 'state:', response['place']['full_name'].split(", ")[1]                
                print 'coordinates:', response['coordinates']
                print 'user:', response['user']
            
        #if ( 'coordinates' in response and response['coordinates'] != None ): print 'coordinates:', response['coordinates']
        #if 'user' in response: 
            #print 'user', response['user']
            #print type(response['user'])
            #print response['user'].keys()
            #print response['user']['created_at']
        

if __name__ == '__main__':
    main()