class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Note:
            - "1" = land
            - "0" = water
            - counter and return total number of islands
            - edges are water
            - Contstraints:
                - max 100 x 100 grid
        Intuition:
            - DFS:
                - initialize starting grid:
                    - r = 0
                    - c = 0
                - recurse 4 directions:
                    - right
                    - down
                    - left
                    - up
                - recursion function:
                    - update cell[r][c] to "0" to indicate that it's visited
                    - check 4 directions:
                        - right
                            - if 0 <= c + 1 <= columns and grid[r][c+1] == "1":
                                return dfs(r, c + 1)
                        - down
                            - if 0 <= r + 1 <= rows and grid[r+1][c] == "1":
                                return dfs(r+1, c)
                        - left
                            - if 0 <= c - 1 <= columns and grid[r][c-1] == "1":
                                return dfs(r, c-1)
                        - up
                            - if 0 <= r - 1 <= rows and grid[r-1][c] == "1":
                                return dfs(r-1, c)
                        - island += 1
        """
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def search(r: int, c: int) -> None:
            grid[r][c] = "0"

            if 0 <= c + 1 < cols and grid[r][c+1] == "1":
                search(r, c+1)
            if 0 <= r + 1 < rows and grid[r+1][c] == "1":
                search(r+1, c)
            if 0 <= c - 1 < cols and grid[r][c-1] == "1":
                search(r, c-1)
            if 0 <= r - 1 < rows and grid[r-1][c] == "1":
                search(r-1, c)



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    search(row, col)
        
        return islands

        