from heapq import heappush, heappop

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan(state):
    d = 0
    for i, value in enumerate(state):
        if value != 0:
            goal = GOAL.index(value)
            d += abs(i // 3 - goal // 3) + abs(i % 3 - goal % 3)
    return d

def solve(start):
    pq = [(manhattan(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        if state == GOAL:
            return path + [state]

        zero = state.index(0)
        row, col = divmod(zero, 3)

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_zero = nr * 3 + nc
                new_state = list(state)
                new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
                new_state = tuple(new_state)

                if new_state not in visited:
                    heappush(pq, (g + 1 + manhattan(new_state),
                                  g + 1, new_state, path + [state]))

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
solution = solve(start)

print("8-Puzzle Solution:")
for state in solution:
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()
