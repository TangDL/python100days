import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    num1= str(sys.stdin.readline().strip())
    num2= str(sys.stdin.readline().strip())

    num2 = sorted(num2)
    for i in range(len(num2)-1):
        k = i+1
        while num2[i] < num1[i] and k<len(num2):
            num2[i], num2[k] = num2[k], num2[i]
            k += 1
        if num2[i] > num1[i]:
            break
    num2 = ''.join(x for x in num2)
    if num1>=num2:
        res = -1
    else:
        res = num2
    sys.stdout.write("%d"%int(res))