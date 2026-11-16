class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a, b, c = False, False, False
        ta, tb, tc = target

        for i, j, k in triplets:
            if i == ta and j <= tb and k <= tc:
                a = True
            if j == tb and i <= ta and k <= tc:
                b = True
            if k == tc and i <= ta and j <= tb:
                c = True

        return a and b and c
        