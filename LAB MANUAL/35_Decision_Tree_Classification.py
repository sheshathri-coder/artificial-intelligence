from sklearn.tree import DecisionTreeClassifier
X=[[1,1],[1,2],[2,1],[8,8],[9,8],[8,9]]; y=[0,0,0,1,1,1]
m=DecisionTreeClassifier(random_state=42).fit(X,y)
print('Prediction:',m.predict([[8,8]]))
# Output: Prediction: [1]