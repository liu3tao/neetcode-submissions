class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        # sort and check repeats.
        nums.sort()
        prevNum = nums[0]
        for n in nums[1:]:
            if prevNum == n:
                return True
            prevNum = n
        return False