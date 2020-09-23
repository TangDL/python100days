# 溢出判断
# 全零
def helper(nums):
    n =len(nums)
    flag = 1
    for i in range(n-2, -1, -1):
        if flag:
            dic = []
            for pos in range(i+1, n):
                dic.append((nums[pos], pos))
            dic = sorted(dic)
            for j in range(len(dic)):
                if nums[i]<dic[j][0]:
                    temp = nums[i]
                    nums[i] = dic[j][0]
                    nums[dic[j][1]] = temp
                    nums[i+1:] = sorted(nums[i+1:])
                    flag = 0
                    break
    return nums

if __name__=="__main__":
    nums = [1, 2, 3]
    res = helper(nums)
    print(res)