class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        firstPass = []
        balance = 0
        for x in s:
            if balance == 0 and x == ")":
                continue
            else:
                if x == "(":
                    balance += 1
                elif x == ")":
                    balance -= 1

                firstPass.append(x)
        ret = []
        balance = 0
        for x in firstPass[::-1]:
            if balance == 0 and x == "(":
                continue
            else:
                if x == "(":
                    balance += 1
                elif x == ")":
                    balance -= 1
                ret.append(x)
        return "".join(ret[::-1])