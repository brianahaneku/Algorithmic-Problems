class Solution:
    def findIntegers(self, n: int) -> int:
        num = n
        bits = []
        while num > 0:
            bits.append(num & 1)
            num >>= 1

        dp = [0 for _ in range(len(bits))]
        dp[0] = 1
        if len(dp) > 1:
            dp[1] = 2
        for i in range(2, len(bits)):
            dp[i] = dp[i - 1] + dp[i - 2]

        ret = 0
        i = len(bits) - 1
        while i >= 0:
            if bits[i] == 1:
                ret += dp[i]
            i -= 1
            if i < len(bits) - 2 and bits[i + 1] == 1 and bits[i + 2] == 1:
                return ret
        return ret + 1
        
