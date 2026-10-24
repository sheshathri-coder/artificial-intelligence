# 4. Alpha-Beta Pruning

def alphabeta(depth, node, alpha, beta, maximizing):
    if depth == 0: return node
    if maximizing:
        v=max(alphabeta(depth-1,node-1,alpha,beta,False),alphabeta(depth-1,node+1,alpha,beta,False))
        return v
    return min(alphabeta(depth-1,node-1,alpha,beta,True),alphabeta(depth-1,node+1,alpha,beta,True))
print('Best value:',alphabeta(2,5,float('-inf'),float('inf'),True))
# Output:
# Best value: 5