import numpy as np
ratings=np.array([[5,4,0],[4,5,0],[0,4,5]])
scores=ratings.sum(axis=0)
recommended=int(np.argmax(scores))
print('Recommended item:',recommended+1)
# Output: Recommended item: 3