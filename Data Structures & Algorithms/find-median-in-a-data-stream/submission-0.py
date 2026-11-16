class MedianFinder:

    def __init__(self):
        self.small = [] # max heap 
        self.big = [] # min heap
        

    def addNum(self, num: int) -> None:

        if self.small and num < -self.small[0]:
            heapq.heappush(self.small, -num)
        elif self.big and num > self.big[0]:
            heapq.heappush(self.big, num)
        else:
            heapq.heappush(self.small, -num)
        
        if len(self.small) == len(self.big) + 2:
            num = -heapq.heappop(self.small)
            heapq.heappush(self.big, num)
        
        if len(self.big) == len(self.small) + 2:
            num = heapq.heappop(self.big)
            heapq.heappush(self.small, -num)

    def findMedian(self) -> float:
        if len(self.big) > len(self.small):
            return self.big[0]
        elif len(self.small) > len(self.big):
            return -self.small[0]
        else:
            return (-self.small[0] + self.big[0])/ 2.0
        
        
        