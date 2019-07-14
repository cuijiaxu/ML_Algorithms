from jieba.analyse import *

with open('sample.txt') as f:
    data = f.read()

#tf-idf
for keyword, weight in extract_tags(data,topK=None, withWeight=True):
    print('%s %s' % (keyword,weight))

#textrank
for keyword,weight in textrank(data, withWeight=True):
    print('%s %s' % (keyword,weight))
