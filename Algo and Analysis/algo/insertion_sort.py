



def insertion_sort(l):
    comparisons = 0
    for i in range(len(l)):
        for j in range(i-1, -1, -1):
            comparisons += 1
            if l[j+1] < l[j]:
                l[j+1], l[j] = l[j], l[j+1]
            else:
                break
    return comparisons
    
l = [23, 23, 23, 23, 23, 23, 23, 23]
print(f"Testing {l}")
print(insertion_sort(l))
print(l)

l = [14, 40, 31, 28, 3, 15, 17, 51]
print(f"Testing {l}")
print(insertion_sort(l))
print(l)
