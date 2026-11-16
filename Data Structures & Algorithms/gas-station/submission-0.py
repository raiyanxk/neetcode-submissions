class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        res = 0
        amt = 0

        for i in range(len(gas)):
            amt += gas[i] - cost[i]

            if amt < 0:
                res = i + 1
                amt = 0
        return res        