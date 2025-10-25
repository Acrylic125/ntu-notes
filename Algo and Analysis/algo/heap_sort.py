
def fix_heap(l, i):
    # Check if its leaf.
    if i > (len(l) // 2):
        return 
    left_i = i * 2 
    right_i = left_i + 1

    smaller_i = left_i
    # Guaranteed to have left child due to earlier check 
    # but may not have right child.
    if right_i <= len(l) and l[left_i-1] > l[right_i-1]:
        smaller_i = right_i
    
    if l[i-1] < l[smaller_i-1]:
        return

    l[smaller_i - 1], l[i - 1] = l[i - 1], l[smaller_i - 1]
    fix_heap(l, smaller_i)

def heapify(l, i):
    # Check if its leaf.
    if (i) > (len(l) // 2):
        return 
    left_i = (i) * 2 
    right_i = left_i + 1

    heapify(l, left_i)
    heapify(l, right_i)

    fix_heap(l, i)

def push_to_heap(l, k):
    l.append(k)
    heapify(l, 1)

def pop_heap(l):
    popped = l.pop(0)
    heapify(l, 1)
    return popped

l = [7, 3, 1, 5, 6, 3, 0, -3, 7]
print(f"Sorting {l}")
heapify(l, 1)
print(f"Heapified {l}")
while len(l) > 0:
    print(pop_heap(l))

l = [8, 7, 6, 5, 4, 3, 2, 1]
print(f"Sorting {l}")
heapify(l, 1)
print(f"Heapified {l}")
push_to_heap(l, 3)
print(f"After pushing 3: {l}")
push_to_heap(l, -10)
print(f"After pushing -10: {l}")

while len(l) > 0:
    print(pop_heap(l))
