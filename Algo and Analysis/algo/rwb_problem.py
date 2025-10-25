


 


def rwb_sort(l):
    R_head = -1
    W_head = -1
    B_head = -1

    for i in range(len(l)):
        e = l[i]
        if e == 'R':
            if R_head == -1:
                R_head = i 
        if e == 'W':
            if W_head == -1:
                W_head = i 
            if i > 0:
                if l[i - 1] == 'B':
                    # Swap B and white
                    l[i - 1], l[i] = l[i], l[i - 1]
                    # B_head += 1
        if e == 'B':
            if B_head == -1:
                B_head = i 
    return l


# s = "RRBBWRBW"
s = "BBWWBBWW"
l = s.split()
print(f"l = {l}")
print(rwb_sort(l))
