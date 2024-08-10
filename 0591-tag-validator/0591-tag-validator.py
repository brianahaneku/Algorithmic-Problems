from enum import Enum

class State(Enum):
    TAG_NAME_START = 1
    TAG_CONTENT_START = 2
    TAG_CONTENT_END = 3
    CDATA_START = 4

class Solution:
    def isValid(self, code: str) -> bool:
        print(len(code))
        if code[0] != '<':
            return False
        n = len(code)
        i = 0
        state = State.TAG_NAME_START
        stack = deque()
        contentDeep = 0
        while i < n:
            #print(i)
            if state == State.TAG_NAME_START:
                if code[i] != '<':
                    return False
                j = code.find('>', i + 1)
                if j == -1 or (not 1 <= j - i - 1 <= 9):
                    return False
                for ix in range(i + 1, j):
                    if (not code[ix].isalpha()) or code[ix].islower():
                        return False
                stack.append(code[i + 1: j])
                state = State.TAG_CONTENT_START
                i = j + 1
            elif state == State.TAG_CONTENT_START:
                if code[i: i + 9] == '<![CDATA[':
                    j = code.find(']]>', i + 9)
                    if j == -1:
                        return False
                    i = j + 3
                    #print(state)
                elif code[i: i + 2] == '</':
                    state = State.TAG_CONTENT_END
                    i = i + 2
                elif code[i] == '<':
                    contentDeep += 1
                    state = State.TAG_NAME_START
                else:
                    i += 1
            elif state == State.TAG_CONTENT_END:
                j = code.find('>', i + 1)
                #print(j, 'here')
                if j == -1:
                    return False
                name = code[i: j]
                if name != stack[-1]:
                    return False
                stack.pop()
                i = j + 1
                if contentDeep > 0:
                    state = State.TAG_CONTENT_START
                    contentDeep -= 1
                else:
                    return i == n
