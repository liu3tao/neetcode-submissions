
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # Sol1: sort and check repeats.
        # if len(nums) <= 1:
        #     return False
        # nums.sort()
        # prevNum = nums[0]
        # for n in nums[1:]:
        #     if prevNum == n:
        #         return True
        #     prevNum = n
        # return False
        
        # Sol2: use dict (hashtable)
        cntDict = {}
        for n in nums:
            if n in cntDict:
                return True
            else:
                cntDict[n] = 1
        return False