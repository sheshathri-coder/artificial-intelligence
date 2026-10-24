from sklearn.svm import SVC
X=[[1,1],[2,2],[8,8],[9,9]]; y=[0,0,1,1]
m=SVC().fit(X,y)
print('Prediction:',m.predict([[8,8]]))
# Output: Prediction: [1]