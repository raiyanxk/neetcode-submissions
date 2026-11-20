class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        
        for s in stones:
            heapq.heappush(heap, -s)
        

        while len(heap) > 1:
            r1 = -1 * heapq.heappop(heap)
            r2 = -1 * heapq.heappop(heap)

            if r1 != r2:
                heapq.heappush(heap, -1 * abs(r1 - r2))
            
        return -1 * heap[0] if len(heap) == 1 else 0

