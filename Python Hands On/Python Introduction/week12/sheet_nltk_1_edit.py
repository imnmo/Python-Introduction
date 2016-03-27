from nltk.corpus import brown

from nltk import FreqDist

genres=['humor','romance','adventure']


for g in genres:
    words=brown.words(categories = g) #Contains all categories in a  single shot
    fdist=FreqDist([w for w in words])
    print (g,fdist)
    fdist.plot(50,cumulative=True)

#print(words)#Contains all  words of these categories
#fdist = FreqDist(words)
#print(fdist)
    #fdist.plot()
    
#for i in fdist:
    #Onetext.append(i)
    #print(Onetext[0])
