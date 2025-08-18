from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 0:
        return arr
    l = 0
    r = len(arr) - 1
    pivot = (r - l) // 2 + l

    less, more = [], []
    for i, x in enumerate(arr):
        if i == pivot:
            continue
        if x < arr[pivot]:
            less.append(x)
        else:
            more.append(x)
    new_list = quick_sort(less) + [arr[pivot]] + quick_sort(more)

    return new_list

arr = [2, 4, 1, 7, 8, 3, 5, 6]
print(quick_sort(arr))



