#!/usr/bin/env python3

from heapq import *

# MinHeap
min_heap = []
heappush(min_heap, 7)
heappush(min_heap, 1)
heappush(min_heap, 2)
heappush(min_heap, 8)
print("MinHeap")
print(min_heap)
print("pop: %d" % heappop(min_heap))
print(min_heap)

#MaxHeap
l = [7, 1, 2, 8]
max_heap = []
for i in l:
	heappush(max_heap, (-i, i))

print("MaxHeap")
print(max_heap)
print("pop: %d" % heappop(max_heap)[1])
print(max_heap)
