class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        r = 0
        c = 0
        for cmd in commands:
            if cmd == 'UP':
                r -= 1
            elif cmd == 'RIGHT':
                c += 1
            elif cmd == 'LEFT':
                c -= 1
            else:
                r += 1
        return r * n + c