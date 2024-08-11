class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ret = 1
        last = s[0]
        length = 1
        for char in s[1:]:
            if ord(char) == ord(last) + 1:
                length += 1
            else:
                ret = max(ret, length)
                length = 1
            last = char
        return max(ret, length)