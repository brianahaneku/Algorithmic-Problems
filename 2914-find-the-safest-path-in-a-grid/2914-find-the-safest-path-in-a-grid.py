from heapq import heappop, heappush
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n=len(grid)
        d=[[float('inf') for _ in range(n)] for __ in range(n)]
        agenda=[[]]
        seen=set()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    agenda[-1].append((i,j))
                    d[i][j]=0
                    seen.add((i,j))
        
        directions = ((-1,0),(1,0),(0,-1),(0,1))
        while agenda[-1]:
            agenda.append([])
            for i,j in agenda[-2]:
                for dx,dy in directions:
                    x,y= i+dx, j+dy
                    if (x,y) in seen:
                        continue
                    if (0<=x<n and 0<=y<n):
                        seen.add((x,y))
                        d[x][y]=len(agenda) - 1
                        agenda[-1].append((x,y))
        
        seen=set()
        pq = deque([(d[0][0], 0, 0)])
        dist = [[0 for _ in range(n)] for __ in range(n)]
        dist[0][0] = d[0][0]
        while pq:
            safeness, i, j = pq.popleft()
            if safeness != dist[i][j]:
                continue
            for dx, dy in directions:
                a, b = i + dx, j + dy
                if 0 <= a < n and 0 <= b < n:
                    s = min(safeness, d[a][b])
                    if s > dist[a][b]:
                        if s == safeness:
                            pq.appendleft((s, a, b))
                        else:
                            pq.append((s, a, b))
                        dist[a][b] = s

        return dist[n - 1][n - 1]