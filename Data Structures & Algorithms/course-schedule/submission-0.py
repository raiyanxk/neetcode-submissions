class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # [0, 1]: take 1 before 0

        graph = collections.defaultdict(list)
        ins = [0] * numCourses
        q = collections.deque()
        seen = set()

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
            
            for next_course in graph[course]:
                ins[next_course] -= 1
                if ins[next_course] == 0:
                    q.append(next_course)

        return len(seen) == numCourses


        