class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        MOD = 10**9 + 7
        def solve(i, a, b):
            if (i, a, b) in dp:
                return dp[(i, a, b)]
            if i == n:
                return 1
            dp[(i, a, b)] = 0
            for c in range(nums[i], a - 1, -1):
                if nums[i] - c > b:
                    break
                dp[(i, a, b)] = ((solve(i + 1, c, nums[i] - c)) + dp[(i, a, b)]) % MOD
            return dp[(i, a, b)]
        return solve(0, 0, 50)
