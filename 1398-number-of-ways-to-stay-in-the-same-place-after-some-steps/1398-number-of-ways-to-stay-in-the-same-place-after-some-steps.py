MOD = 10**9 + 7
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        m = min(steps, arrLen)
        prev = [0 for _ in range(m)]
        prev[0] = 1
        for s in range(1, steps + 1):
            temp = []
            for i in range(m):
                val = prev[i]
                if i > 0:
                    val = (val + prev[i - 1]) % MOD
                if i < m - 1:
                    val = (val + prev[i + 1]) % MOD
                temp.append(val)
            prev = temp[::]
        return prev[0]