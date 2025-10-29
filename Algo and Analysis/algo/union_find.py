from typing import List, Tuple

def union_find(n: int, instructions: List[Tuple[int, int]], weighted=True, compression=True):
    id = [i for i in range(n)]
    sz = [1] * n

    def find(v: int):
        if not compression:
            while id[v] != v:
                v = id[v]
            return v
        if id[v] != v:
            id[v] = find(id[v])
        return id[v]

    def union(r1: int, r2: int):
        nonlocal sz, id
        if r1 == r2:
            return

        if weighted:
            if sz[r1] < sz[r2]:
                id[r1] = r2
                sz[r2] += sz[r1]
            else:
                id[r2] = r1
                sz[r1] += sz[r2]
        else:
            id[r2] = r1

    for a, b in instructions:
        r1 = find(a)
        r2 = find(b)
        union(r1, r2)

    return id, sz

edges = [(0, 1), (1, 2), (3, 4)]
id, sz = union_find(5, edges)
print("Parents:", id)
print("Sizes:", sz)
