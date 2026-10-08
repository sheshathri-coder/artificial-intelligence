from itertools import permutations

def tsp(graph):
    n = len(graph)
    cities = range(1, n)
    best_cost = float("inf")
    best_route = None

    for perm in permutations(cities):
        route = (0,) + perm + (0,)
        cost = sum(graph[route[i]][route[i+1]] for i in range(n))

        if cost < best_cost:
            best_cost = cost
            best_route = route

    return best_route, best_cost

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

route, cost = tsp(graph)

print("Travelling Salesman Solution:")
print("Route:", " -> ".join(str(city + 1) for city in route))
print("Minimum Cost:", cost)
