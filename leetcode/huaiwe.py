

def main():
    nums = [1, 2, 8, 4, 4, 1, 3, 4]
    k = 8
    n = len(nums)
    if n == 0:
        return 0
    summ = 0
    dictt = {0: -1}
    res = 0
    for i in range(n):
        summ += nums[i]
        try:
            if (dictt[summ - k]): res = max(res, i - dictt[summ-k])
        except:
            dictt[summ] = i
    return res

if __name__=="__main__":
    res = main()
    print(res)


