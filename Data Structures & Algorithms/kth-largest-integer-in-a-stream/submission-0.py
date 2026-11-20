class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for num in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, num)
            elif num > self.heap[0]:
                heapq.heappush(self.heap, num)
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)            

        return self.heap[0]       

