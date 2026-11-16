class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = [0] * 26
        time = 0
        q = [] # (timestamp_available, count)

        for c in tasks:
            counts[ord(c) - ord('A')] += 1
        
        heap = []
        q = collections.deque()

        for c in counts:
            if c > 0:
                heap.append(-c)

        heapq.heapify(heap)

        while heap or q:
            time += 1

            if not heap:
                time = q[0][0]
            else:
                count = -heapq.heappop(heap)
                if count > 1:
                    q.append([time + n, count - 1])
            
            if q and q[0][0] == time:
                _, count = q.popleft()
                heapq.heappush(heap, (-count))


        

        return time





        