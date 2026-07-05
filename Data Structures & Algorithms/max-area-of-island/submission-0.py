class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows=len(grid)
        cols=len(grid[0])

        vis = [[0]*cols for _ in range(rows)]

        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        
        ans=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and vis[r][c]==0:
                    
                    area = self.bfs(r,c,vis,grid,directions,rows,cols)
                    ans = max(area,ans)
        return ans

    def bfs(self,r,c,vis,grid,directions,rows,cols):
        q=deque()
        q.append((r,c))
        vis[r][c]=1
        area=1
        while q:

            i,j = q.popleft()
            for dx,dy in directions:
                nx,ny=i+dx,j+dy

                if nx<0 or ny<0 or nx>=rows or ny>=cols:
                    continue
                
                if grid[nx][ny]==1 and vis[nx][ny]==0:
                    q.append((nx,ny))
                    vis[nx][ny]=1
                    area+=1
        return area