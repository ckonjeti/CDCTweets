#TODO: Add dates for data, Figure out which criteria to write to CSV file

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
j = 0
maxTweets = 5
#Start and end dates for range of dates for twitter data collection
startDate = "2015-09-10"
endDate = "2015-09-12"
#tweetCriteria = got.manager.TweetCriteria().setQuerySearch(keywords[i]).setSince(startDate).setUntil(endDate).setMaxTweets(5)
#tweet = got.manager.TweetManager.getTweets(tweetCriteria)[j] 
#criteria = [keywords[i], tweet.username, tweet.retweets, tweet.text]
#finds maxTweets number of tweets for each keyword and writes to CSV file
for i in range(5):
    for j in range(maxTweets):
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(keywords[i]).setMaxTweets(5)
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)[j] 
        row = [repr(s).encode("utf-8") for s in [keywords[i], tweet.username, tweet.text, tweet.date, tweet.retweets, tweet.mentions, tweet.hashtags]]
        #print(tweet)
        dataWriter.writerow(row)






