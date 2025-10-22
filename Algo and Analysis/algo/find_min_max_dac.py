


def find_min_max(l):
    if len(l) <= 0:
        raise RuntimeError("Shouldnt have happened.")
        # return ()
    if len(l) == 1:
        return (l[0], l[0])
    if len(l) == 2:
        if l[0] < l[1]:
            return (l[0], l[1])
        return (l[1], l[0])
    mid = len(l) // 2
    min1, max1 = find_min_max(l[0:mid])
    min2, max2 = find_min_max(l[mid:])
    min = min1 if min1 < min2 else min2
    max = max1 if max1 > max2 else max2
    return (min, max)
    

print(find_min_max([1, 2, 3, 4, 5, 6, 7, 8]))
