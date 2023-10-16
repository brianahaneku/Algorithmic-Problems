GENE_LENGTH = 8
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        if end not in bank:
            return -1
        validGenes = set(bank)
        pq = [[start]]
        seen = {start}
        while pq:
            if len(pq) > len(bank):
                return -1
            pq.append([])
            for gene in pq[-2]:
                for char in "ACGT":
                    for ix in range(GENE_LENGTH):
                        newGene = gene[:ix] + char + gene[ix + 1:]
                        if newGene in validGenes and newGene not in seen:
                            if newGene == end:
                                return len(pq) - 1
                            seen.add(newGene)
                            pq[-1].append(newGene)
        
        return -1