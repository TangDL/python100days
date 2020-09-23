import string
class Solution:
    def modifyString(self, s: str) -> str:
        res = list('0'+s+'0')
        n = len(res)
        temp = string.ascii_lowercase
        for i in range(1, res-1):
            if i=='?':
                for j in temp:
                    if res[i-1] != j and res[i+1] != j:
                        res[i] = j
                        break
        return ''.join(res[1:-1])

print(string.ascii_lowercase[0])