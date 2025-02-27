import matplotlib.pyplot as plt
from functools import lru_cache

def count_paths(input_string):
    # Convert the input string into a grid
    grid = [list(row.split()) for row in input_string.strip().split('\n')]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Find start (A) and end (B) positions, and identify blocked paths
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

    # Visualizing the grid with matplotlib
    def plot_grid():
        fig, ax = plt.subplots()
        ax.set_xticks(range(cols))
        ax.set_yticks(range(rows))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xlim(-0.5, cols - 0.5)
        ax.set_ylim(rows - 0.5, -0.5)

        # Color the grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'A':
                    ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, color='green', label='Start'))
                elif grid[i][j] == 'B':
                    ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, color='red', label='Goal'))
                elif grid[i][j] == 'x':
                    ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, color='black', label='Obstacle'))
                else:
                    ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, color='white', label='Free Path'))

        plt.show()

    plot_grid()  # Visualize the grid before starting pathfinding
    return backtrackpath(A, frozenset({A}))

# Example Input
input_string = 'A . . .\n. . . .\n. . . .\n. . x B'
paths = count_paths(input_string)

print(f"The number of paths will be: {paths}")
