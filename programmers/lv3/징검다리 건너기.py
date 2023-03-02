from heapq import heappop, heappush

def solution(stones, k):
    q = []
    ans = 200000000
    for i in range(k - 1):
        heappush(q, (-stones[i], i))
    
    for i in range(k - 1, len(stones)):
        heappush(q, (-stones[i], i))
        
        while q[0][1] < i - k + 1:
            heappop(q)
        ans = min(ans, -q[0][0])
        
    return ans