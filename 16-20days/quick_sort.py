def quick_sort(arr):
    if len(arr) < 2:
        return arr
    piovt = arr[-1]
    left = [x for x in arr if x < piovt]
    middle = [x for x in arr if x == piovt]
    right = [x for x in arr if x > piovt]
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_1(arr):
    if len(arr) < 2:
        return arr
    piovt = arr[-1]
    k = -1
    for index, value in enumerate(arr):
        if value < piovt:
            k += 1
            arr[k], arr[index] = arr[index], arr[k]
    arr[k+1], arr[-1] = arr[-1], arr[k+1]
    return quick_sort_1(arr[:k]) + [piovt] + quick_sort_1(arr[k+2:])
