import heapq

nums = [2, 3, 1, 1, 5, 5, 4]
k = 3

max_heap = []

for ele in nums:
    max_heap.append(ele)

heapq.heapify(max_heap)
print(max_heap)

while len(max_heap) > k:
    heapq.heappop(max_heap)
print(max_heap[0])
