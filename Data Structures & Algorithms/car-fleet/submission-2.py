class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = 0
        prev = -1
        ps = [(p,s) for p,s in zip(position, speed)]
        ps.sort(reverse=True) # sort by increasing position and speed

        for p, s in ps:
            finish_time = (target - p) / s

            if finish_time > prev:
                fleets += 1
                prev = finish_time


        return fleets