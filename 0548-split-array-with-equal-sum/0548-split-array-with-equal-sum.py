class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        prefix = [0]
        for i, num in enumerate(nums):
            prefix.append(prefix[-1] + num)
        evenSplitSums = [set() for _ in range(n)]
        for i in range(2, n):
            for j in range(i - 1):
                if prefix[j + 1] == prefix[i + 1] - prefix[j + 2]:
                    evenSplitSums[i].add(prefix[j + 1])
        for k in range(n - 2, 4, -1):
            sum4 = prefix[n] - prefix[k + 1]
            for j in range(k - 2, 2, -1):
                sum3 = prefix[k] - prefix[j + 1]
                if sum3 != sum4:
                    continue
                if sum3 in evenSplitSums[j - 1]:
                    return True
        return False
