import sys
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got
import re
import sys,codecs,csv 
import functions as f

#opens file and splits every word by the delimiter OR
filename = "C:\Users\Chaitu Konjeti\CDCTweets\Keywords.txt"


keywords = f.sortKeyword(filename)


def printTweet(descr, t):
	print(descr)
	print("Username: %s" % t.username)
	print("Retweets: %d" % t.retweets)
	print("Text: %s" % t.text)
	print("Mentions: %s" % t.mentions)
	print("Hashtags: %s\n" % t.hashtags)


tweetCriteria = got.manager.TweetCriteria()

#Output file initialization
outputFileName = "output_got.csv"
outputFile = codecs.open(outputFileName, "w+", "utf-8")
dataWriter = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

i = 0
maxTweets = 1
posts = []
#finds maxTweets number of tweets for each keyword and writes to CSV file
for i in range(len(keywords)):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(keywords[i]).setSince("2010-01-01").setUntil("2010-06-01").setMaxTweets(maxTweets)
    if(len(got.manager.TweetManager.getTweets(tweetCriteria)) != 0):
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)
        posts.append(tweet)
#print(posts)
for line in posts:
    #print(line)
    for i in range(len(line)):
        #printTweet('tweet', line[i])
        row = [repr(s).encode("utf-8") for s in [line[i].username, line[i].retweets, line[i].text, line[i].id, line[i].permalink, line[i].date, line[i].favorites, line[i].mentions, line[i].hashtags, line[i].geo]]
        dataWriter.writerow(row)