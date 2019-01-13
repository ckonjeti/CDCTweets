#with open("C:\Users\Chaitu Konjeti\GetOldTweets-python\Keywords.txt") as f:
#    content = f.readlines()
##    for line in f:
##        content = line.split()
#    #print (content)
#    wordList = []
#    a = content[0].split("OR")
#    wordList.append(a)
#    #wordList.append(1)
#    print(wordList)
    
    
#row = []
#wordFile = open("C:\Users\Chaitu Konjeti\GetOldTweets-python\Keywords.txt", 'r')
#for line in wordFile.readlines():
#    row.append([line])
#    for i in line.split("OR"):
#        row[-1].append(i)
#print (row[0])

#wordFile = open("C:\Users\Chaitu Konjeti\GetOldTweets-python\Keywords.txt", 'r')
#yourResult = [line.split('OR') for line in wordFile.readlines()]
#print(yourResult[0])
filename = "C:\Users\Chaitu Konjeti\GetOldTweets-python\Keywords.txt"
keywords = []
with open(filename, 'r') as f:
    for line in f:
        for word in line.split('OR'):
            keywords.append(str(word))
            
