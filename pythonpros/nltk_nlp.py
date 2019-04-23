import nltk

text = "let us test nlp of nltk"
sens = nltk.sent_tokenize(text)

words = []
for sent in sens:
    words.append(nltk.word_tokenize(sent))

print(words)