class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # need to get the sorted indices of nums.
        sortedIds = sorted(range(len(nums)), key=lambda k: nums[k])
        # two pointers, shift left and right until they meet.
        left = 0
        right = len(nums) - 1
        while left < right:
            lIdx = sortedIds[left]
            rIdx = sortedIds[right]
            sum = nums[lIdx] + nums[rIdx]
            if sum > target:
                right -= 1
            elif  sum < target:
                left += 1
            else:
                return sorted([lIdx, rIdx])
        return []