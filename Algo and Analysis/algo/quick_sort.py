



def quick_sort(l):
    if len(l) == 0:
        return [], 0
    if len(l) == 1:
        return [l[0]], 0
    pivot_i = len(l) // 2

    comparisons = 0
    left, right = [], []
    for i in range(len(l)):
        comparisons += 1
        if i == pivot_i:
            continue
        if l[i] < l[pivot_i]:
            left.append(l[i])
        else:
            right.append(l[i])

    l1, c1 = quick_sort(left)
    l2, c2 = quick_sort(right)

    return [*l1, l[pivot_i], *l2], c1 + c2 + comparisons

l = [23, 23, 23, 23, 23, 23, 23, 23]
print(f"Testing {l}")
print(quick_sort(l))

l = [14, 40, 31, 28, 3, 15, 17, 51]
print(f"Testing {l}")
print(quick_sort(l))
