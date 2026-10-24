from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
X=[[1],[2],[3],[8],[9],[10]]; y=[0,0,0,1,1,1]
g=GridSearchCV(DecisionTreeClassifier(random_state=42),{'max_depth':[1,2,3]},cv=2).fit(X,y)
print('Best parameters:',g.best_params_)
# Output: Best parameters: {'max_depth': 1}