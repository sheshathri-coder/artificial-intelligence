import random
states=['Sunny','Rainy']; trans={'Sunny':['Sunny','Rainy'],'Rainy':['Sunny','Rainy']}
s='Sunny'; seq=[s]
for _ in range(4): s=random.choice(trans[s]); seq.append(s)
print('Sequence:',seq)
# Output: Sequence: ['Sunny', 'Sunny', 'Rainy', 'Sunny', 'Rainy']