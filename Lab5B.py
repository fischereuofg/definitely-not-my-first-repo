import string
inString=str(input())

inString=str(inString.lower())

inString=str(inString.replace(',', ''))
inString=str(inString.replace('.', ''))

wordList=[]
frequency=[]
wordTuple=[] 
wordList=inString.split(' ')
for i in range(len(wordList)):
    if wordList[i] in wordTuple:
        pos=wordTuple.index(wordList[i])
        frequency[pos]+=1

    else:
        wordTuple.append(wordList[i])
        frequency.append(1)

for p in range(len(wordTuple)):
    print(str(wordTuple[p])+": "+str(frequency[p]))