import random
w=[random.random() for _ in range(3)]
for _ in range(100):
    w=[x+(1-x)*0.1 for x in w]
fitness=-sum((x-1)**2 for x in w)
print('Weights:',[round(x,2) for x in w])
print('Fitness:',round(fitness,2))
# Output: Weights: [1.0, 1.0, 1.0]
# Fitness: 0.0