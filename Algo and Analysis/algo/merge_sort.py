


def merge_sort(l):
    if len(l) == 1:
        return [l[0]], 0
    comparisons = 0
    mid = len(l) // 2
    n1, c1 = merge_sort(l[:mid])
    n2, c2 = merge_sort(l[mid:])

    nL = []
    while len(n1) > 0 and len(n2) > 0:
        comparisons += 1
        if n1[0] < n2[0]:
            nL.append(n1.pop(0))
        else:
            nL.append(n2.pop(0))

    nL.extend(n1)
    nL.extend(n2)
    return nL, comparisons + c1 + c2

l = [23, 23, 23, 23, 23, 23, 23, 23]
print(f"Testing {l}")
print(merge_sort(l))
print()

l = [14, 40, 31, 28, 3, 15, 17, 51]
print(f"Testing {l}")
print(merge_sort(l))
print()
