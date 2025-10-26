from typing import List

def top_sort(E):
    sort_graph = []
    def dfs(v):
        nonlocal sort_graph
        if v in sort_graph:
            return
        for neighbour_i in range(len(E)):
            if E[v][neighbour_i] > 0:
                dfs(neighbour_i)
        sort_graph = [v, *sort_graph]
    for i in range(len(E)):
        dfs(i)
    return sort_graph

# Accepts partial solutions.
def is_valid_top_sort(solution, E):
    visited = set()
    for i in range(len(solution) - 1, -1, -1):
        cur_i = solution[i]
        # All its children must already be visited.
        for child_i in range(len(E)):
            # If not, then reject.
            if E[cur_i][child_i] == 1 and child_i not in visited:
                return False
        # All its parents MUST NOT be visited.
        for parent_i in range(len(E)):
            # If not, then reject.
            if E[parent_i][cur_i] == 1 and parent_i in visited:
                return False
        visited.add(cur_i)
    # Otherwise, accept.
    return True

def graph_search(E, parent: List[int]):
    solutions = []

    if len(parent) >= len(E):
        return [parent]
    
    for i in range(len(E)):
        if i not in parent:
            candidate = [i, *parent] 
            if is_valid_top_sort(candidate, E):
                sub_solutions = graph_search(E, candidate)
                for sol in sub_solutions:
                    solutions.append(sol)
    return solutions

# Graph 1: Simple linear dependency chain (5 nodes)
# 0 -> 1 -> 2 -> 3 -> 4
graph1 = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
]
print(f"Graph: {graph1}")
print(f"Top Sorted: {top_sort(graph1)}")


# Graph 2: Tree-like structure (6 nodes)
#     0
#    / \
#   1   2
#  / \   \
# 3   4   5
graph2 = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
print(f"Graph: {graph2}")
print(f"Top Sorted: {top_sort(graph2)}")

# Graph 3: Complex DAG (7 nodes)
# Multiple paths and dependencies
#   0 -> 1 -> 3 -> 5
#   |    |    |    |
#   v    v    v    v
#   2 -> 4 -------> 6
graph3 = [
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
]
print(f"Graph: {graph3}")
print(f"Top Sorted: {top_sort(graph3)}")

graph4 = [
    # A  B  C  D  E  F  G  H
    [0, 0, 0, 0, 0, 0, 0, 0],  # A
    [1, 0, 0, 0, 1, 0, 0, 0],  # B -> A, E
    [0, 0, 0, 1, 0, 0, 0, 1],  # C -> D, H
    [0, 1, 0, 0, 0, 0, 0, 0],  # D -> B
    [0, 0, 0, 0, 0, 1, 0, 0],  # E -> F
    [0, 0, 0, 0, 0, 0, 0, 0],  # F
    [1, 0, 0, 0, 0, 0, 0, 0],  # G -> A
    [0, 1, 0, 0, 0, 0, 1, 0]   # H -> B, G
]
chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print(f"Graph: {graph4}")
sorted_graph = top_sort(graph4)
print(f"Top Sorted: {list(map(lambda i: chars[i], sorted_graph))}")
print(f"Is valid?: {is_valid_top_sort(sorted_graph, graph4)}")
solutions = graph_search(graph4, [])
print(f"Total possible solutions: {len(solutions)}")
for sol in solutions:
    print(f"{list(map(lambda i: chars[i], sol))} is_valid? {is_valid_top_sort(sol, graph4)}")


