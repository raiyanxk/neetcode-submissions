class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [(p, s) for p, s in zip(position, speed)]
        ps.sort(reverse=True)

        prev = (target - ps[0][0]) / ps[0][1]
        res = 1

        for i in range(1, len(ps)):
            p, s = ps[i]
            time = (target - p) / s

            if time > prev:
                res += 1
                prev = max(prev, time)


        return res
        