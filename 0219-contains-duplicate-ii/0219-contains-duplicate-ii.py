class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        freq = collections.defaultdict(int)

        for i in range(min(k + 1, n)):
            freq[nums[i]] += 1
            if freq[nums[i]] > 1:
                return True

        for i in range(k + 1, n):
            freq[nums[i - k - 1]] -= 1
            freq[nums[i]] += 1
            if freq[nums[i]] > 1:
                return True
        return False
     