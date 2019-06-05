
from nltk.tokenize import sent_tokenize,word_tokenize

example_text="""Hello Mr. Smith,How are you doing today?
The Weather is great and python is awesome.
The sky is pinkish blue.
"""

print("Word Tokenizer")
print(word_tokenize(example_text))

print("Sentence Tokenizer")
print(sent_tokenize(example_text))
