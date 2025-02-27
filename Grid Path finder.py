def count_paths(input_string):
    from functools import lru_cache

    grid = [list(row.split()) for row in input_string.strip().split('\n')]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    A = None
    B = None
    blocked_path = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A':
                A = (i, j)
            elif grid[i][j] == 'B':
                B = (i, j)
            elif grid[i][j] == 'x':
                blocked_path.add((i, j))
    if not A or not B:
        return 0
    total_points = rows * cols - len(blocked_path)
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    @lru_cache(maxsize=None)
    def backtrackpath(current, visited):
        if current == B:
            return 1 if len(visited) == total_points else 0
        count = 0
        for direction in directions:
            new_i, new_j = current[0] + direction[0], current[1] + direction[1]
            if 0 <= new_i < rows and 0 <= new_j < cols:
                if (new_i, new_j) not in blocked_path and (new_i, new_j) not in visited:
                    count += backtrackpath((new_i, new_j), visited | {(new_i, new_j)})
        return count

    return backtrackpath(A, frozenset({A}))

input_string = 'A . . .\n. . . .\n. . . .\n. . x B'
paths = count_paths(input_string)
print("The number of paths will be:")
print(paths) 