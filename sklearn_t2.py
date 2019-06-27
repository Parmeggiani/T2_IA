import pandas as pd
from io import StringIO
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import chi2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('corpus_lema.csv')
df.head()

col = ['PERGUNTAS','CLASSES']
df = df[col]
df = df[pd.notnull(df['PERGUNTAS'])]
df.columns = ['PERGUNTAS','CLASSES']
df['class_id'] = df['CLASSES'].factorize()[0]
class_id_df = df[['CLASSES', 'class_id']].drop_duplicates().sort_values('class_id')
class_to_id = dict(class_id_df.values)
id_to_category = dict(class_id_df[['class_id', 'CLASSES']].values)
df.head()

## GRAFICO

# fig = plt.figure(figsize=(8,6))
# df.groupby('CLASSES').PERGUNTAS.count().plot.bar(ylim=0)
# plt.show()

##

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=4, max_df=0.75, norm='l2', encoding='latin-1', ngram_range=(1,2))
features = tfidf.fit_transform(df.PERGUNTAS).toarray()
labels = df.class_id
features.shape

model =  RandomForestClassifier()
X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(features, labels, df.index, test_size=0.2, random_state=0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

target_names = df['CLASSES'].value_counts().index.tolist()

print((metrics.classification_report(y_test, y_pred, target_names=target_names, labels=range(len(target_names)))))