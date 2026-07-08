class Solution:
    # b*c = a*b*c - (a-1)*b*c
    # no, I still need to know b*c.
    # wait, can we use the previous result?
    # b*c, a*c, a*b
    # OK, just need to multiply the current number with n in all the other slots.
    # 1, a, a
    # b, a, a*b
    # b*c, a*c, a*b
    # no, that's O(n^2)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        sur = [1] * len(nums)
        # 1, a, a*b
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        # b*c, c, 1
        for i in range(len(nums) - 2, -1, -1):
            sur[i] = sur[i+1] * nums[i+1]
        res = []
        for i in range(len(nums)):
            res.append(pre[i] * sur[i])
        return res




        