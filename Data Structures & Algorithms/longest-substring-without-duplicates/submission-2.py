class Solution:
    # Use a set to track the non-repeating substring
    # Need l, r to set a window.
    # Move r until there is a dup
    # then move l until the dup is skipped.
    def lengthOfLongestSubstring(self, s: str) -> int:
        charLoc = {}
        maxL = 0
        l, r = 0, 0
        while r < len(s):
            c = s[r]
            while c in charLoc:
                charLoc.pop(s[l])
                l += 1
            charLoc[c] = r
            r += 1
            maxL = max(maxL, r - l)
        return maxL
