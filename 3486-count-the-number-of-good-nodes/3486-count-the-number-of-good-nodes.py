class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        ans = 0
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        seen = {0}
        def solve(u):
            nonlocal ans
            sizes = []
            total = 1
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    size = solve(v)
                    total += size
                    sizes.append(size)
            if len(set(sizes)) <= 1:
                
                ans += 1
            return total
        solve(0)
        return ans

