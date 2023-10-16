class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        rows = []
        n, m = len(num1), len(num2)
        
        for i in range(m - 1, -1, -1):
            rows.append([0] * (m - i - 1))
            carry = 0
            for j in range(n - 1, -1, -1):
                product = int(num2[i]) * int(num1[j]) + carry
                if j > 0:
                    rows[-1].append(product % 10)
                    carry = product // 10
                elif product < 10:
                    rows[-1].append(product)
                else:
                    rows[-1].append(product % 10)
                    rows[-1].append(product // 10)
            
        k = len(rows[-1])
        carry = 0
        ret = ""
        for i in range(k):
            result = carry
            j = m - 1
            while j >= 0 and i < len(rows[j]):
                result += rows[j][i]
                j -= 1
            if i < k - 1:
                ret = str(result % 10) + ret
                carry = result // 10
            else:
                ret = str(result) + ret
        return ret