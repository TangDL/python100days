

def main():

    n = 12
    nums = [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100]
    cont = [(nums[i], i) for i in range(n)]

    dp = [0] * n

    res = 0
    i = 2
    while i < len(cont):
        maxn = max(cont[:i])
        minn = min(cont[:maxn[1]])
        print(maxn, cont[:maxn[1]])
        if (maxn[0] - minn[0]) > 0:
            res += (maxn[0] - minn[0])
            cont.remove(maxn)
            cont.remove(minn)
            cont[:][1] -= 2
            # print(cont)
        else: i += 1
    return res

res = main()
print(res)
