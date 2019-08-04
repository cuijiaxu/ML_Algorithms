import pandas as pd
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score

df = pd.read_csv('loans.csv')
X=df.drop('safe_loans',axis=1)
Y=df.safe_loans
d=defaultdict(LabelEncoder)
X_trans = X.apply(lambda x: d[x.name].fit_transform(x))

X_train,X_test,Y_train,Y_test = train_test_split(X_trans,Y,random_state=1)
clf = tree.DecisionTreeClassifier(max_depth=3)
clf = clf.fit(X_train,Y_train)

'''
展示决策树
with open("safe-loans.dot", 'w') as f:
     f = tree.export_graphviz(clf,
                              out_file=f,
                              max_depth = 3,
                              impurity = True,
                              feature_names = list(X_train),
                              class_names = ['not safe', 'safe'],
                              rounded = True,
                              filled= True )

from subprocess import check_call
check_call(['dot','-Tpng','safe-loans.dot','-o','safe-loans.png'],shell=True)

from PIL import Image, ImageDraw, ImageFont
img = Image.open("safe-loans.png")
draw = ImageDraw.Draw(img)
img.save('output.png')
img1 = Image.open('output.png')
img1.show()
'''

a = accuracy_score(Y_test,clf.predict(X_test))

print(a)