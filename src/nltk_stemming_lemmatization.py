
"""" stop words removal example"""
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

example_text="""Hello Mr. Smith,How are you doing today?
The Weather is great and python is awesome.
The sky is pinkish blue.
"""

tokens=word_tokenize(example_text)

porterStemmer=PorterStemmer()

stemmed_tokens=[porterStemmer.stem(token) for token in tokens]

print(stemmed_tokens)

wordNetLemmatizer=WordNetLemmatizer()

lemmas=[wordNetLemmatizer.lemmatize(token,pos=wordnet.VERB) for token in tokens]

print(lemmas)