import random
pop=[random.randint(0,10) for _ in range(20)]
for _ in range(50):
    pop.sort(key=lambda x:-(x-5)**2+25,reverse=True)
    pop=pop[:10]+[random.randint(0,10) for _ in range(10)]
best=max(pop,key=lambda x:-(x-5)**2+25)
print('Best value:',best); print('Fitness:',-(best-5)**2+25)
# Output: Best value: 5
# Fitness: 25