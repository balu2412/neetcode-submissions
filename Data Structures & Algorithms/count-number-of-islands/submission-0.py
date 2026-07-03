class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count=0
        rows=len(grid)
        cols=len(grid[0])
        visited=[[0]*cols for _ in range(rows)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and visited[r][c]==0:
                    count+=1
                    self.dfs(r,c,visited,directions,grid,rows,cols)
        return count
    def dfs(self,r,c,visited,directions,grid,rows,cols):
        q=deque()
        q.append((r,c))
        visited[r][c]=1
        while q:
            i,j=q.popleft()
            for dx,dy in directions:
                new_i,new_j=i+dx,j+dy

                if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols:
                    continue

                if grid[new_i][new_j]=="1" and visited[new_i][new_j]==0:
                    q.append((new_i,new_j))
                    visited[new_i][new_j]=1
