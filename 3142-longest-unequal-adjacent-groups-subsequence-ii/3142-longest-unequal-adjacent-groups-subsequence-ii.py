class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        def ham(w1,w2):
            if len(w1) != len(w2):
                return 0
            ct = 0 
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    ct += 1
                    if ct > 1:
                        return 0
            return ct
                    
        dpCount = [1 for _ in range(n + 1)]
        dpCount[-1] = 0
        parent = [None for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if ham(words[i], words[j]) == 1 and groups[i] != groups[j]:
                    if 1 + dpCount[j] > dpCount[i]:
                        dpCount[i] = 1 + dpCount[j]
                        parent[i] = j 
       
        
        ix = 0
        for i in range(n):
            if dpCount[i] > dpCount[ix]:
                ix = i
        ret = []
        ret.append(words[ix])
        while parent[ix] != None:
            ix = parent[ix]
            ret.append(words[ix])
        return ret
                    
        