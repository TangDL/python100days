def solution(n):
    # write code here
    temp = n
    nums = []
    while temp > 9:
        flag = 0
        for i in range(9, 1, -1):
            if temp % i == 0:
                flag = 1
                nums.append(i)
                temp /= i
                if temp < 10:
                    nums.append(int(temp))
                break
        if flag == 0:
            return -1
    print(nums)
    nums = sorted(nums)
    print(nums)
    res = ''.join(str(x) for x in nums)
    print(res)
    return int(res)

solution(123456789)