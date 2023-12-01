from collections import deque

def calc_neighbors(grid):
    neighbors = {}
    row_count = len(grid)
    col_count = len(grid[0])
    
    for row_idx, row in enumerate(grid):
        for col_idx, _ in enumerate(row):
            directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]
            neighbors[(row_idx, col_idx)] = []

            for d in directions:
                new_row = row_idx + d[0]
                new_col = col_idx + d[1]
                # I hate whitespace formatted conditionals
                # If we are in bounds and If neighbor is at most 1 above
                if 0 <= new_row < row_count and 0 <= new_col < col_count and grid[row_idx][col_idx] >= grid[new_row][new_col] - 1:
                    neighbors[(row_idx, col_idx)].append((new_row, new_col))
    return neighbors  

def traverse_graph(grid, neighbors, start_loc, end_loc):
    scores = []

    visited = set()
    queue = deque([(start_loc, 0)])
    
    while queue:
        (c, cs) = queue.popleft()
        if c in visited:
            continue

        visited.add(c)

        if c == end_loc:
            scores.append(cs)

        for n in neighbors[c]:
            # If haven't visited this node yet, visit it
            queue.append((n, cs + 1))

    if len(scores) == 0:
        return 1_000_000_000

    return min(scores)


with open('input.txt') as f:
    grid = []
    start_loc = []
    end_loc = []
    for row_idx, row in enumerate(f.readlines()):
        grid.append([])
        for col_idx, ch in enumerate(row.strip()):
            num = None
            if ch == 'E':
                num = ord('z')
                end_loc = (row_idx, col_idx)
            elif ch == 'S':
                start_loc = (row_idx, col_idx)
                num = ord('a')
            else:
                num = ord(ch)
            num -= ord('a')
            grid[row_idx].append(num)
    
    neighbors = calc_neighbors(grid)
    print(traverse_graph(grid, neighbors, start_loc, end_loc))



with open('input.txt') as f:
    grid = []
    start_locs = []
    end_loc = []
    for row_idx, row in enumerate(f.readlines()):
        grid.append([])
        for col_idx, ch in enumerate(row.strip()):
            num = None
            if ch == 'E':
                num = ord('z')
                end_loc = (row_idx, col_idx)
            elif ch == 'S':
                start_locs.append((row_idx, col_idx))
                num = ord('a')
            else:
                if ch == 'a':
                    start_locs.append((row_idx, col_idx))
                num = ord(ch)
            num -= ord('a')
            grid[row_idx].append(num)
    
    neighbors = calc_neighbors(grid)
    scores = []
    for start_loc in start_locs:
        scores.append(traverse_graph(grid, neighbors, start_loc, end_loc))
    print(min(scores))