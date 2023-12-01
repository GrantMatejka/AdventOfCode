def print_grid(grid):
    for i, row in enumerate(grid):
        print(i, " ", end="")
        for x in row:
            print(x, end="")
        print()


def build_grid1(paths):
    minX = min(sum([[point[0] for point in path] for path in paths], []))
    maxX = max(sum([[point[0] for point in path] for path in paths], [])) - minX + 1
    maxY = max(sum([[point[1] for point in path] for path in paths], [])) + 1
    normalized_paths = [
        [[point[1], point[0] - minX] for point in path] for path in paths
    ]
    sand_src = [0, 500 - minX]

    grid = [["." for _ in range(maxX)] for _ in range(maxY)]

    for path in normalized_paths:
        starting_point = path[0]
        for idx in range(1, len(path)):
            next_point = path[idx]

            deltaRow = next_point[0] - starting_point[0]
            deltaCol = next_point[1] - starting_point[1]

            while not starting_point == next_point:
                grid[starting_point[0]][starting_point[1]] = "#"

                if not starting_point[0] == next_point[0]:
                    dir = int(deltaRow / abs(deltaRow))
                    starting_point[0] += dir

                if not starting_point[1] == next_point[1]:
                    dir = int(deltaCol / abs(deltaCol))
                    starting_point[1] += dir

            grid[starting_point[0]][starting_point[1]] = "#"
            starting_point = path[idx]

    return (grid, sand_src)


def fall_dir(grid, sp):
    new_row = sp[0] + 1
    if new_row >= len(grid) or sp[1] - 1 < 0 or sp[1] + 1 >= len(grid[0]):
        return "OOB"
    if grid[new_row][sp[1]] == ".":
        return "D"
    elif grid[new_row][sp[1] - 1] == ".":
        return "DL"
    elif grid[new_row][sp[1] + 1] == ".":
        return "DR"
    else:
        return False


with open("input.txt") as f:
    paths = [
        [[int(n) for n in p.strip().split(",")] for p in l.strip().split("->")]
        for l in f.readlines()
    ]
    (grid, sand_src) = build_grid1(paths)

    sand = 0
    x = True
    while x:
        # Drop sand
        sand += 1
        sp = sand_src.copy()
        fall = fall_dir(grid, sand_src)
        while not fall == False:
            if fall == "OOB":
                print(sand - 1)
                x = False
                break

            # change grid back to air
            grid[sp[0]][sp[1]] = "."

            sp[0] += 1

            # Don't need to check
            if fall == "DL":
                sp[1] -= 1
            elif fall == "DR":
                sp[1] += 1

            grid[sp[0]][sp[1]] = "O"

            fall = fall_dir(grid, sp)


def build_grid2(paths):
    maxY = max(sum([[point[1] for point in path] for path in paths], [])) + 2
    normalized_paths = [[[point[1], point[0]] for point in path] for path in paths]

    blockers = set()

    for path in normalized_paths:
        starting_point = path[0]
        for idx in range(1, len(path)):
            next_point = path[idx]

            deltaRow = next_point[0] - starting_point[0]
            deltaCol = next_point[1] - starting_point[1]

            while not starting_point == next_point:
                blockers.add(tuple(starting_point))

                if not starting_point[0] == next_point[0]:
                    dir = int(deltaRow / abs(deltaRow))
                    starting_point[0] += dir

                if not starting_point[1] == next_point[1]:
                    dir = int(deltaCol / abs(deltaCol))
                    starting_point[1] += dir

            blockers.add(tuple(starting_point))
            starting_point = path[idx]

    return (blockers, maxY)


def fall_dir2(blockers, floor, sp):
    new_row = sp[0] + 1
    d_blocked = (new_row, sp[1]) in blockers
    dl_blocked = (new_row, sp[1] - 1) in blockers
    dr_blocked = (new_row, sp[1] + 1) in blockers

    # can't fall below floor limit
    if new_row >= floor:
        return False

    if not d_blocked:
        return "D"
    if not dl_blocked:
        return "DL"
    if not dr_blocked:
        return "DR"
    return False


with open("input.txt") as f:
    # Represent the grid as a list of points for blockers
    # then iterate by dropping sand and checking list of blockers
    paths = [
        [[int(n) for n in p.strip().split(",")] for p in l.strip().split("->")]
        for l in f.readlines()
    ]
    (blockers, floorY) = build_grid2(paths)

    sand = 0
    sand_src = (0, 500)
    while True:
        # Drop sand
        sand += 1
        sp = sand_src
        fall = fall_dir2(blockers, floorY, sand_src)
        blockers.add(sp)

        while not fall is False:
            blockers.remove(sp)

            sp = (sp[0] + 1, sp[1])

            # Don't need to check
            if fall == "DL":
                sp = (sp[0], sp[1] - 1)
            elif fall == "DR":
                sp = (sp[0], sp[1] + 1)

            fall = fall_dir2(blockers, floorY, sp)
            blockers.add(sp)

        if sp == sand_src:
            break

    print(sand)
