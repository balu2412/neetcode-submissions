from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visited = [[0] * cols for _ in range(rows)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(r, c):

            q = deque()
            q.append((r, c))
            visited[r][c] = 1

            perimeter = 0

            while q:

                i, j = q.popleft()

                for dx, dy in directions:

                    nx = i + dx
                    ny = j + dy

                    if (nx < 0 or ny < 0 or
                        nx >= rows or ny >= cols or
                        grid[nx][ny] == 0):

                        perimeter += 1

                    elif visited[nx][ny] == 0:

                        visited[nx][ny] = 1
                        q.append((nx, ny))

            return perimeter

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    return bfs(r, c)

        return 0