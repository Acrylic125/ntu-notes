import heapq

arr = [4, 2, 7, 1, 3, 5, 8, 6]
print(arr)
heapq.heapify(arr)
print(arr)  
sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
print(sorted_arr)

