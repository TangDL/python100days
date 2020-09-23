def fib(num, temp={}):
    if num in (1, 2):
        return 1
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib(num - 1) + fib(num - 2)
        return temp[num]


def max_sum_value_of_sublist():
    arr = list(map(int, input().split()))
    size = len(arr)
    overall, partial = {}, {}
    overall[size-1] = partial[size-1] = arr[-1]
    for i in range(size - 2, -1, -1):
        partial[i] = max(arr[i], arr[i] + partial[i+1])
        overall[i] = max(partial[i], overall[i+1])
    print(overall[0])

if __name__=='__main__':
    max_sum_value_of_sublist()