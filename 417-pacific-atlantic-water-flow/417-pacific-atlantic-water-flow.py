class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        m, n = len(heights), len(heights[0])
        def bfs(reachable_ocean):
            q = collections.deque(reachable_ocean)
            while q:
                (i,j) = q.popleft()
                for (di, dj) in [(0,1), (1,0), (0,-1), (-1,0)]:
                    ni, nj = i + di, j+ dj
                    if 0 <= ni < m and 0<=nj<n and (ni, nj) not in reachable_ocean \
                    and heights[i][j] <= heights[ni][nj]:
                        q.append((ni, nj))
                        reachable_ocean.add((ni, nj))
            return reachable_ocean
        pacific = set( [(i,0) for i in range(m)] + [(0,j) for j in range(1,n)])
        atlantic = set( [(i, n-1) for i in range(m)] + [(m-1,j) for j in range(n-1)])
        return list(bfs(pacific) & bfs(atlantic))