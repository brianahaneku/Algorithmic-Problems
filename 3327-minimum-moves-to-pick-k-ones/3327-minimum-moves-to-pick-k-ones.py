def kClosest(nums, x, k):
    l = 0
    r = len(nums) - k
    while l <= r:
        m = (l + r) // 2
        right = nums[m + k] if m + k < len(nums) else float('inf')
        if abs(nums[m] - x) > abs(right - x):
            l = m + 1
        else:
            r = m - 1
    return l

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        n = len(nums)
        ones = []
        for i, x in enumerate(nums):
            if x:
                ones.append(i)
        prefix = [0]
        for x in ones:
            prefix.append(prefix[-1] + x)
        ret = float('inf')
        for i in range(n):
            picked = 0
            if nums[i]:
                picked += 1
            if picked == k:
                return 0
            ops = 0
            for ix in i - 1, i + 1:
                if 0 <= ix < n and nums[ix]:
                    picked += 1
                    ops += 1
                    if picked == k:
                        break
            if picked == k:
                ret = min(ops, ret)
                continue
            elif maxChanges >= k - picked:
                ops += (k - picked) * 2
                ret = min(ops, ret)
                continue
            else:
                ops += maxChanges * 2
                picked += maxChanges
                size = k - picked
                for ix in range(i - 1, i + 2):
                    if 0 <= ix < n and nums[ix]:
                        size += 1
                index = kClosest(ones, i, size)
                endIndex = index + size - 1
                l = index
                r = endIndex
                while l <= r:
                    m = (l + r) // 2
                    if ones[m] <= i:
                        l = m + 1
                    else:
                        r = m - 1
                if l < index:
                    ops += prefix[endIndex + 1] - prefix[index] - (endIndex - index) * i
                    if i + 1 < n and nums[i + 1] and index <= i + 1 <= endIndex:
                        ops -= 1
                elif l > endIndex:
                    ops += (endIndex - index) * i - (prefix[endIndex + 1] - prefix[index])
                    if i - 1 >= 0 and nums[i - 1] and 0 <= i - 1 <= endIndex:
                        ops -= 1
                else:
                    ops += prefix[endIndex + 1] - prefix[l] - (endIndex - l + 1) * i
                    if l - 1 >= index and ones[l - 1] < i:
                        ops += (l - index) * i - (prefix[l] - prefix[index])
                    elif l - 2 >= index:
                        ops += (l - 1 - index) * i - (prefix[l - 1] - prefix[index])
                    for ix in i - 1, i + 1:
                        if ones[index] <= ix <= ones[endIndex] and nums[ix]:
                            ops -= 1
                    ret = min(ret, ops)
        return ret
