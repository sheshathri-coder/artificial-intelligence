from sklearn.cluster import KMeans
X=[[1],[2],[3],[8],[9],[10]]
m=KMeans(n_clusters=2,random_state=42,n_init=10).fit(X)
print('Labels:',m.labels_)
# Output: Labels: [1 1 1 0 0 0]