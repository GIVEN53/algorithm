from sys import stdin
from heapq import heappush, heappop


max_heap = []
min_heap = []
for _ in range(int(stdin.readline())):
    x = int(stdin.readline())

    if len(max_heap) == len(min_heap):
        heappush(max_heap, x * -1)
    else:
        heappush(min_heap, x)

    if len(max_heap) > 0 and len(min_heap) > 0 and max_heap[0] * -1 > min_heap[0]:
        mx = heappop(max_heap) * -1
        mn = heappop(min_heap)

        heappush(max_heap, mn * -1)
        heappush(min_heap, mx)

    print(max_heap[0] * -1)

##########################
#    memory: 37132KB     #
#    time:   260ms       #
##########################
