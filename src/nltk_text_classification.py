import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

# just get the first 3000 most frequent words (if we haven't got stop words 1000 must have been sufficient)
word_features = list(all_words.keys())[:3000]
# print(word_features)

def find_features(document_words):
    document_words=set(document_words)    #removing multiple occurences
    features={}

    for word in word_features:     #for all words which are features ( top 3000)
        if(word in document_words):        # if that word is in document
            features[word]=1            # keep that in dictionary with 1
        else:
            features[word]=0            # keep that in dictionary with 0

    return features

#Now lets create whole featureSet
feature_set=[(find_features(document_words),category) for (document_words,category) in documents]
print(feature_set[0])

