import sys
import math


def get_factor(num):
    list0 = []
    temp = 2
    if num == temp:
        list0.append(temp)
    else:
        while(num>=temp):
            k = num%temp
            if k==0:
                list0.append(temp)
                num = num/ temp
            else:
                temp = temp+1
    return list0

def is_primer(N):
    if N<=1:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if N%i==0:
            return False
    return True



if __name__=="__main__":
    ss = list(map(int, sys.stdin.readline().strip().split()))
    S, E = ss[0], ss[1]
    yushu = []
    if not is_primer(E): #不是质数
        citys = get_factor(E)
        citys = set(citys)
        print(citys)

        for city in citys:
            yushu.append(S%city)
        time = min(yushu)
    else:
        citys1 = set(get_factor(E+1))
        citys2 = set(get_factor(E-1))
        for city in citys1:
            yushu.append(S%city)
        for city in citys2:
            yushu.append(S%city)
        time = min(yushu) +1
    sys.stdout.write("%d"%time)





