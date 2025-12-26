def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r, c):
        # stop if out of bounds or water
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] == '0':
            return

        # mark land as visited
        grid[r][c] = '0'

        # visit neighbours
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)

    return islands
