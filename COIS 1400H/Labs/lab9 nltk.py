# Punyaja Mishra
# 0660001
# Lab9 : Natural Languagwhe Processing Tasks

import nltk
#nltk.download()
from nltk.corpus import stopwords, gutenberg
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import re

#stopwords & punctuations
stop_words = set(stopwords.words('english'))
punctuations = [".", "!", "?", ",", ";", ":", "-", "[", "]", "{", "}", "(", ")", "/", "*", "~",
"<", ">", "`", "^", "_", "|", "#", "$", "%", "+", "=", "&", "@", " ", "'"] 

#getting macbeth.txt
mac_text = nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')

#list containing non stopwords
mylist = []

# a lop to go through each word, convert it to lower() since it is case sensitive & then
# checking if is is in the stopwords && punctuations; if not then append it to the list
for word in mac_text:
    if (word.lower() not in stop_words) and (word not in punctuations):
        mylist.append(word)

#print the list - its a lot of data so will be squeezed i output
print(mylist)

#frequency
data_analysis = nltk.FreqDist(mylist)
print(data_analysis)

#print most common words form the no stop words list
print("Most common words in Macbeth (excluding stopwords & punctuations) : ")
print(data_analysis.most_common)




