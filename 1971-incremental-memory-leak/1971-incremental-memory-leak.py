class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        bits = 1
        while bits <= memory1 or bits <= memory2:
            if memory1 >= memory2:
                memory1 -= bits
            else:
                memory2 -= bits
            bits += 1
        return [bits, memory1, memory2]