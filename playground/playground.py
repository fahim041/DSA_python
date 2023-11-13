def dfs_shortest_path(grid):
    ROWS, COLS = len(grid), len(grid[0])

    def dfs_helper(r, c, visit):
        if(
            min(r, c) < 0 or 
            r == ROWS or c == COLS or
            (r, c) in visit or 
            grid[r][c] == 1
        ):
            return float("inf")
        
        if r == ROWS - 1 and c == COLS - 1:
            return 0
        
        visit.add((r, c))
        
        min_route = float("inf")
        min_route = min(min_route, 1 + dfs_helper(r + 1, c, visit))
        min_route = min(min_route, 1 + dfs_helper(r - 1, c, visit))
        min_route = min(min_route, 1 + dfs_helper(r, c + 1, visit))
        min_route = min(min_route, 1 + dfs_helper(r, c - 1, visit))

        visit.remove((r, c))
        return min_route

    visit = set()
    result = dfs_helper(0, 0, visit)
    
    return result

# Example usage:
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

result = dfs_shortest_path(grid)
print(result)
