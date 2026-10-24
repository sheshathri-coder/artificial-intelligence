from sklearn.linear_model import LinearRegression
X=[[1],[2],[3],[4]]; y=[3,5,7,9]
m=LinearRegression().fit(X,y)
print('Prediction:',m.predict([[5]])[0])
# Output:
# Prediction: 11.0