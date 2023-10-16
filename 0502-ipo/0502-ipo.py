from heapq import heappop, heappush
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(capital)
        join = [(capital[i], profits[i]) for i in range(n)]
        join.sort()
        pq = []
        ix = 0

        while ix < n and join[ix][0] <= w:
            heappush(pq, -join[ix][1])
            ix += 1

        while (pq or (ix < n and join[ix][0] <= w)) and k > 0:
            if ix < n and join[ix][0] <= w:
                heappush(pq, -join[ix][1])
                ix += 1
            else:
                w += -heappop(pq)
                k -= 1

        return w