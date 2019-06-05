
"""" stop words removal example"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_text="""Hello Mr. Smith,How are you doing today?
The Weather is great and python is awesome.
The sky is pinkish blue.
"""

tokens=word_tokenize(example_text)

# getting all stop words of english language
english_stopwords=set(stopwords.words("english"))


filtered_tokens=list(filter(lambda token: token not in english_stopwords,tokens))
neglected_tokens=list(filter(lambda token: token in english_stopwords,tokens))

print(len(tokens))
print(len(filtered_tokens))

print(neglected_tokens)
print(filtered_tokens)