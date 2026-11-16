class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # [0, 1]
        # take course 1 before course 0
        # 1 -> 0

        res = []
        seen = set()
        q = collections.deque()
        graph = collections.defaultdict(list)
        ins = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            ins[course] += 1
        
        for i in range(len(ins)):
            if ins[i] == 0:
                q.append(i)
        
        while q:
            
            course = q.popleft()

            if course in seen:
                continue
            
            seen.add(course)
            res.append(course)
            
            for neighbor in graph[course]:
                ins[neighbor] -= 1
                if ins[neighbor] == 0:
                    q.append(neighbor)

        return res if len(res) == numCourses else []
        