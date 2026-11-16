class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        res = [-1] * len(arr)

        top = -1

        for i in range(len(arr) -1, -1, -1):
            res[i] = top
            top = max(top, arr[i])


        return res 
        