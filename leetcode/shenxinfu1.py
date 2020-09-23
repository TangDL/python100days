import sys

def helper(string):
    num_s, num_w, num_r =0, 0, 0
    res = 0
    for i in string:
        if i=='s' and num_w == 0:
            num_s+=1
        if i=='w' and num_s > 0:
            num_w += 1
        if i == 'r' and num_s >0 and num_w > 0:
            num_r += 1
            res += num_s * num_w
    return res

if __name__=="__main__":
    n = int(sys.stdin.readline().strip())
    strings  = []
    for i in range(n):
        strings.append(sys.stdin.readline().strip())
    ress = []
    for strr in strings:
        ress.append(helper(strr))
    for i in range(n):
        k = ress[i] % 1000000007
        sys.stdout.write("%d" % k)
        if i != n-1:
            sys.stdout.write("\n")