import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import gutenberg

sample_text=example_text= """Hello Mr. Smith,How are you doing today?
The Weather is great and python is awesome.
The sky is pinkish blue.
"""

# we could also have used .words() to get list of words
# bible_words=gutenberg.words("bible-kjv.txt")

tokens=word_tokenize(sample_text)

pos_tagged_tokens=nltk.pos_tag(tokens)

for tagged in pos_tagged_tokens:
    print(tagged)


