from typing import List

class Solution1:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        res = []
        croak = 'croak'
        for i in croakOfFrogs:
            print(res)
            if i not in croak:
                return -1
            if i == 'c' and '' not in res:
                res.append('c')
                continue
            flag = 1
            for j in range(len(res)):
                temp_res_j = res[j] + i
                if temp_res_j == croak:
                    res[j] = ''
                    flag = 0
                    break
                elif temp_res_j in croak and temp_res_j.startswith('c'):
                    res[j] = res[j] + i
                    flag = 0
                    break
            if flag: return -1
        print(res)
        for i in res:
            if i != '': return -1
        return len(res)


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c, r, o, a, k = 0, 0, 0, 0, 0
        res, now = 0, 0
        for i in croakOfFrogs:
            if i == 'c':
                c += 1
                now += 1
                res = max(res, now)
            elif i == 'r':
                r += 1
            elif i == 'o':
                o += 1
            elif i == 'a':
                a += 1
            elif i == 'k':
                k += 1
                now -=1
            if not c>=r>=o>=a>=k: return -1
        return res if now == 0 else -1



croakfrogs = "crcoakroak"
s = Solution()
res = s.minNumberOfFrogs(croakfrogs)
print(res)


