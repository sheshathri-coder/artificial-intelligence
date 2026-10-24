# 5. Decision Tree
from sklearn.tree import DecisionTreeClassifier
X=[[0],[1],[2],[3]]; y=['No','No','Yes','Yes']
m=DecisionTreeClassifier(random_state=42).fit(X,y)
print('Prediction:',m.predict([[2]]))
# Output:
# Prediction: ['Yes']