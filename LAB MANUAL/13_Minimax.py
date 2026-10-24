# 3. Minimax Algorithm

def minimax(depth, node, maximizing):
    if depth == 0:
        return node
    if maximizing:
        return max(minimax(depth-1,node-1,False), minimax(depth-1,node+1,False))
    return min(minimax(depth-1,node-1,True), minimax(depth-1,node+1,True))

print('Best value:', minimax(2,3,True))

# Output:
# Best value: 3