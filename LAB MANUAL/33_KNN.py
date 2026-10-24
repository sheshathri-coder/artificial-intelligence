from sklearn.neighbors import KNeighborsClassifier
X=[[1],[2],[3],[8],[9],[10]]; y=[0,0,0,1,1,1]
m=KNeighborsClassifier(n_neighbors=3).fit(X,y)
print('Prediction:',m.predict([[7]]))
# Output:
# Prediction: [1]