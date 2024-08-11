class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        dp = []
        dp = [[0 for _ in range(nums[i] + 1)] for i in range(n)]
        dp.append([0] * 1001)
        prefix = [0]
        for i in range(nums[-1] + 1):
            dp[n][i] = 1
            prefix.append(prefix[-1] + 1)
        for i in range(nums[-1] + 1, 1001):
            prefix.append(prefix[-1])
        
        for i in range(n - 1, -1, -1):
            if i == 0:
                a = 0
                b = nums[0]
                dp[i][a] = (prefix[min(nums[0] + 1, len(prefix) - 1)] - prefix[min(len(prefix) - 1, max(a, nums[i] - b))]) % MOD
                break
            newPrefix = [0]
            for a in range(nums[i] + 1):
                b = nums[i - 1] - a
                if b < 0 or a > nums[i]:
                    dp[i][a] = 0
        
                else:
                    dp[i][a] = (prefix[min(nums[i] + 1, len(prefix) - 1)] - prefix[min(len(prefix) - 1, max(a, nums[i] - b))]) % MOD
                newPrefix.append(newPrefix[-1] + dp[i][a])
            prefix = newPrefix[::]
            
        return dp[0][0]