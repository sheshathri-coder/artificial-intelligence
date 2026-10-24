# 1. Map Coloring to implement CSP
colors=['Red','Green','Blue']
N={'A':['B','C'],'B':['A','C','D'],'C':['A','B','D'],'D':['B','C']}
def solve(a):
    if len(a)==len(N): return a
    r=next(x for x in N if x not in a)
    for c in colors:
        if all(a.get(n)!=c for n in N[r]):
            a[r]=c
            if solve(a): return a
            del a[r]
print(solve({}))
# Output: {'A':'Red','B':'Green','C':'Blue','D':'Red'}