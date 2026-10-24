from sklearn.decomposition import PCA
X=[[1,2,3],[2,3,4],[3,4,5],[4,5,6]]
Z=PCA(n_components=2).fit_transform(X)
print('Output shape:',Z.shape)
# Output: Output shape: (4, 2)