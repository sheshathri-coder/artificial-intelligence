from collections import deque

# State = (missionaries_left, cannibals_left, boat_side)
# boat_side: 0 = left, 1 = right

def safe(m, c):
    return (m == 0 or m >= c) and (3-m == 0 or 3-m >= 3-c)

def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            return path + [state]

        for dm, dc in moves:
            if boat == 0:
                nm, nc = m - dm, c - dc
                nb = 1
            else:
                nm, nc = m + dm, c + dc
                nb = 0

            if 0 <= nm <= 3 and 0 <= nc <= 3 and safe(nm, nc):
                new_state = (nm, nc, nb)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [state]))

solution = solve()

print("Missionaries and Cannibals Solution:")
for state in solution:
    print(state)
