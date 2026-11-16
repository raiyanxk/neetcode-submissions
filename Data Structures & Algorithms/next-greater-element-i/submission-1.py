class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # nums1 is a subset of nums2

        indices = {num: i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []

        for num in nums2:

            while stack and num > stack[-1]:
                small = stack.pop()
                idx = indices[small]
                res[idx] = num


            if num in indices:
                stack.append(num)

        return res


