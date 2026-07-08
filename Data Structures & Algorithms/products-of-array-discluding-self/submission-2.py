class Solution:
    # b*c = a*b*c - (a-1)*b*c
    # no, I still need to know b*c.
    # wait, can we use the previous result?
    # b*c, a*c, a*b
    # OK, just need to multiply the current number with n in all the other slots.
    # 1, a, a
    # b, a, a*b
    # b*c, a*c, a*b
    # no, that's O(n^2). Below is the division based solution.
    # Note that we should not multiple the first 0.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        numZeros = 0
        for n in nums:
            if n == 0:
                numZeros += 1
            else:
                total *= n
        res = [0] * len(nums)
        if numZeros > 1:
            return res
        for i, n in enumerate(nums):
            if numZeros == 1:
                res[i] = total if n == 0 else 0
            else:
                res[i] = total // n
        return res
    # # Standard answer:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     pre = [1] * len(nums)
    #     sur = [1] * len(nums)
    #     # 1, a, a*b
    #     for i in range(1, len(nums)):
    #         pre[i] = pre[i-1] * nums[i-1]
    #     # b*c, c, 1
    #     for i in range(len(nums) - 2, -1, -1):
    #         sur[i] = sur[i+1] * nums[i+1]
    #     res = []
    #     for i in range(len(nums)):
    #         res.append(pre[i] * sur[i])
    #     return res




        