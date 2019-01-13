import sys
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

filename = "C:\Users\Chaitu Konjeti\GetOldTweets-python\Keywords.txt"
keywords = []
with open(filename, 'r') as f:
    for line in f:
        for word in line.split('OR'):
            keywords.append(str(word))
                


def printTweet(descr, t):
	print(descr)
	print("Username: %s" % t.username)
	print("Retweets: %d" % t.retweets)
	print("Text: %s" % t.text)
	print("Mentions: %s" % t.mentions)
	print("Hashtags: %s\n" % t.hashtags)
#num = 0
#for word in keywords:
i = 0
maxTweets = 5
#x = 0
for i in range(len(keywords)):
    for j in range(maxTweets):
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(keywords[i]).setMaxTweets(5)
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)[j] 
        printTweet("Get tweets by query search " + keywords[i], tweet)
   
    
#print(keywords)    



#tweetCriteria = got.manager.TweetCriteria().setUntil("2016-01-31").setQuerySearch("bitcoin").setMaxTweets(10)
#
#for i in range(2):
#    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
#    print(tweet.id)
#    print(tweet.username)
#    print(tweet.text)
#    print(tweet.date)



