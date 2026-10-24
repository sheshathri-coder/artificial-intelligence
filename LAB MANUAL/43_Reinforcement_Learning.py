q={'left':0,'right':0}
q['right'] += 0.5*(1-q['right'])
print('Q values:',q)
print('Best action:',max(q,key=q.get))
# Output:
# Q values: {'left': 0, 'right': 0.5}
# Best action: right