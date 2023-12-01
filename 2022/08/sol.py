with open('input.txt') as f:
    grid = [[int(ch) for ch in line.strip()] for line in f.readlines()]
    visible = 0
    grid_height = len(grid)
    for x in range(grid_height):
        row_width = len(grid[x])
        for y in range(row_width):
            if x + 1 >= grid_height or x - 1 < 0 or y + 1 >= row_width or y - 1 < 0:
                visible += 1
                continue
            else:
                edges = [
                    grid[x][:y],
                    grid[x][y+1:],
                    [grid[i][y] for i in range(x) if i != x],
                    [grid[i][y] for i in range(x, grid_height) if i != x]
                ]

                if any(all(grid[x][y] > n for n in edge) for edge in edges):
                    visible += 1

    print(visible)

with open('input.txt') as f:
    grid = [[int(ch) for ch in line.strip()] for line in f.readlines()]
    max_vis = 0
    grid_height = len(grid)
    for x in range(grid_height):
        row_width = len(grid[x])
        for y in range(row_width):
            left = grid[x][:y]
            left.reverse()
            top = [grid[i][y] for i in range(x) if i != x]
            top.reverse()
            edges = [
                left,
                grid[x][y+1:],
                top,
                [grid[i][y] for i in range(x, grid_height) if i != x]
            ]

            visibility_score = 1
            for edge in edges:
                count = 0
                for tree in edge:
                    count += 1
                    if tree >= grid[x][y]:
                        break

                visibility_score *= count

            if visibility_score > max_vis:
                max_vis = visibility_score

    print(max_vis)
