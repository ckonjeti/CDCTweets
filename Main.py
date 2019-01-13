import sys
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got
import re
import sys,getopt,datetime,codecs,xlsxwriter,csv 
#opens file and splits every word by the delimiter OR
filename = "C:\Users\Chaitu Konjeti\CDCTweets\Keywords.txt"


#final sorted list
keywords = []

#lists used during sorting
preKeywords = []
andList = []
andListNew = []

#sorts into AND and not AND sections
with open(filename, 'r') as f:
    for line in f:
        for word in re.split('\(\(|\)\)',line):
            if str(word).find('AND') > 0:
                andList.append(str(word))
            elif word != ' OR ':
                preKeywords.append(word)
                
#sorts the non AND section and appends the final product to keywords
for x in preKeywords:
    for x in (x.split(' OR ')):
        if x != '':            
            keywords.append(str(x.replace("\"","")))
            
#sorts the AND section into groups            
for x in andList:
    for y in x.split(' AND '):
        andListNew.append(y.replace("(","").replace(")","").replace("\"","").split(" OR "))
     
#sorts the AND section groups and appends the final product to keywords
x = 0
while x < len(andListNew):
    if x % 2 == 0:
        for z in andListNew[x]:
            for y in range(len(andListNew[x + 1])):
                keywords.append((z + ' ' + andListNew[x + 1][y]))
    x += 1             



def printTweet(descr, t):
	print(descr)
	print("Username: %s" % t.username)
	print("Retweets: %d" % t.retweets)
	print("Text: %s" % t.text)
	print("Mentions: %s" % t.mentions)
	print("Hashtags: %s\n" % t.hashtags)


tweetCriteria = got.manager.TweetCriteria()
outputFileName = "output_got.csv"
#workbook = xlsxwriter.Workbook('Tweets.xlsx')
#worksheet = workbook.add_worksheet()
outputFile = codecs.open(outputFileName, "w+", "utf-8")
dataWriter = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

i = 0
maxTweets = 5
row = 0
col = 0

#finds maxTweets number of tweets for each keyword and prints to console
for i in range(5):
    for j in range(maxTweets):
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(keywords[i]).setMaxTweets(5)
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)[j] 
        row = [repr(s).encode("utf-8") for s in [keywords[i], tweet.username, tweet.retweets, tweet.text]]
        dataWriter.writerow(row)
#        
#            
#        row += 1
        #printTweet("Get tweets by query search " + keywords[i], tweet)
   
#workbook.close()





