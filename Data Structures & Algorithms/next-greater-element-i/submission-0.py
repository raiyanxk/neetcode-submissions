class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)

        indices = {num: i for i, num in enumerate(nums1)}

        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]

            while stack and stack[-1] < curr:
                big = stack.pop()
                if big in indices:
                    index = indices[big]
                    res[index] = curr
            
            stack.append(curr)
        
        return res 