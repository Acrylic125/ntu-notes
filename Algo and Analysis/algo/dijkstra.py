def dijkstra(E, source=0):
    INF = None
    n = len(E)
    d = [INF for i in range(n)]
    pi = [INF for i in range(n)]
    d[source] = 0  # Initialize source distance to 0
    S = set()
    
    while len(S) < n:
        lowest_d = None
        lowest_node = None
        
        # Find unvisited node with minimum distance
        for i in range(n):
            if i in S: 
                continue
            if lowest_d is None or (d[i] is not None and d[i] < lowest_d):
                lowest_d = d[i]
                lowest_node = i
        
        # If no reachable node found, break
        if lowest_node is None or lowest_d is None:
            break
        
        S.add(lowest_node)
        neighbours = E[lowest_node]
        
        # Relax edges
        for j in range(len(neighbours)):
            if neighbours[j] is None or j in S:
                continue
            alt = lowest_d + neighbours[j]
            if d[j] is None or alt < d[j]:
                d[j] = alt
                pi[j] = lowest_node
    
    return (d, pi)


# Example usage:
if __name__ == "__main__":
    # Example graph (adjacency matrix)
    # None represents no edge
    graph = [
        [0,    4,    None, None, None, None, None, 8,    None],
        [4,    0,    8,    None, None, None, None, 11,   None],
        [None, 8,    0,    7,    None, 4,    None, None, 2   ],
        [None, None, 7,    0,    9,    14,   None, None, None],
        [None, None, None, 9,    0,    10,   None, None, None],
        [None, None, 4,    14,   10,   0,    2,    None, None],
        [None, None, None, None, None, 2,    0,    1,    6   ],
        [8,    11,   None, None, None, None, 1,    0,    7   ],
        [None, None, 2,    None, None, None, 6,    7,    0   ]
    ]
    
    distances, predecessors = dijkstra(graph, source=0)
    
    print("Distances from source (0):", distances)
    print("Predecessors:", predecessors)
