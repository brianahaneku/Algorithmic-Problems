class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        ret = []
        for x in (0,1):
            prevGroup = x
            seq = []
            for i in range(n):
                if groups[i] != prevGroup:
                    seq.append(words[i])
                    prevGroup = groups[i]
            if len(seq) > len(ret):
                ret = seq[::]
        return ret