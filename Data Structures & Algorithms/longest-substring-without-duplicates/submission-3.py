class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Grow right till a dup is found, then reset left to
        # the last time the dup char is seen.
        left = 0
        right = 0
        foundChars = {}
        maxLen = 0
        while right < len(s):
            currChar = s[right]
            if currChar in foundChars:
                # move left till there is no dup.
                while s[left] != currChar:
                    del foundChars[s[left]]
                    left += 1
                left += 1
                right += 1
            else:
                foundChars[currChar] = right
                right += 1
                maxLen = max(maxLen, right - left)
        return maxLen
            
            
