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
        print response['place'],response['coordinates'],response['user']

if __name__ == '__main__':
    main()