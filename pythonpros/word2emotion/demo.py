import pandas as pd
import jieba
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
from sklearn import metrics

def mark_label(df):
    df["sentiment"] = df["star"].apply(lambda x:1 if x>3 else 0)

def cnSegment(text):
    return " ".join(jieba.cut(text))

def getstopwords(filename):
    with open(filename) as f:
        stopwords = f.read()
    stopwordList = stopwords.split('\n')
    return stopwordList

#读取数据
df = pd.read_csv('data.csv',encoding='gb18030')
#df.shape

mark_label(df)

x = df[["comment"]]
y = df.sentiment
x['cutted_comment'] = x.comment.apply(cnSegment)
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1)

stop_words_file = "stopwords.txt"
stopwords = getstopwords(stop_words_file)

#构建特征向量
vect = CountVectorizer(max_df=0.8,
    min_df=3,
    token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b',
    stop_words=frozenset(stopwords))
term_matrix = pd.DataFrame(vect.fit_transform(x_train.cutted_comment).toarray(),columns=vect.get_feature_names())
print(term_matrix[:5])

#朴素贝叶斯分类
nb = MultinomialNB()
pipe = make_pipeline(vect,nb)
cross_val_score(pipe,x_train.cutted_comment,y_train,cv=5,scoring='accuracy').mean()

pipe.fit(x_train.cutted_comment,y_train)
y_pred = pipe.predict(x_test.cutted_comment)
#metrics.accuracy_score(y_test,y_pred)
a = metrics.confusion_matrix(y_test,y_pred)

print(pipe.predict([cnSegment("太难吃了")]))