class Solution:
    # 2 pointers, move the lower bar in each iteration.
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            a = (r - l) * min(heights[l], heights[r])
            res = max(res, a)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
        