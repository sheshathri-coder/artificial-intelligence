from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
X=['good movie','excellent film','bad movie','terrible film']; y=[1,1,0,0]
v=CountVectorizer(); A=v.fit_transform(X); m=LogisticRegression().fit(A,y)
print('Sentiment:', 'Positive' if m.predict(v.transform(['good film']))[0] else 'Negative')
# Output: Sentiment: Positive