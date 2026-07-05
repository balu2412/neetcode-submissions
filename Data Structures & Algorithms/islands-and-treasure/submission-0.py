class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])

        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        INF= 2147483647

        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))

        while q:
            i,j=q.popleft()

            for dx,dy in directions:
                nx=i+dx
                ny=j+dy

                if nx<0 or nx>=rows or ny<0 or ny>=cols: 
                    continue
                if grid[nx][ny]!=INF:
                    continue

                grid[nx][ny]=grid[i][j]+1
                q.append((nx,ny))


                