class Solution:
    def countAndSay(self, n: int) -> str:
        
        def say(n: int) -> str:
            if n == 1:
                return "1"
            digitString = say(n - 1)
            ret = ""
            i = 0
            j = 1
            while j < len(digitString):
                if digitString[j] != digitString[i]:
                    ret += str(j - i) + str(digitString[i])
                    i = j
                j += 1
            ret += str(j - i) + str(digitString[i])
            return ret
        return say(n)
