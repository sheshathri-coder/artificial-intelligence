from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
X,y=load_digits(return_X_y=True); Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42)
m=MLPClassifier(hidden_layer_sizes=(64,),max_iter=500,random_state=42).fit(Xtr,ytr)
print('Accuracy:',round(m.score(Xte,yte),2))
# Output: Accuracy: 0.97