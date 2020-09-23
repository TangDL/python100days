class Solution:
    def combine(self, n: int, k: int):
        if n < k: return []
        if n == 0: return []

        res = []
        self.backtrack(n, k, res, [], 1)
        return res

    def backtrack(self, n, k, res, temp, start):
        if len(temp) == k:
            res.append(temp[:])
            return
        for i in range(start, n + 1):
            if k-len(temp) > n-i+1:
                break
            temp.append(i)
            self.backtrack(n, k, res, temp, i + 1)
            temp.pop()

if __name__ == "__main__":
    s = Solution()
    res = s.combine(0, 0)
    print(res)
