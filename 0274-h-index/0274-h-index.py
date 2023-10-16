class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        hIndex = 1 if citations[-1] > 0 else 0
        for ix, x in enumerate(citations):
            hIndex = max(hIndex, min(x, n - ix))
        return hIndex