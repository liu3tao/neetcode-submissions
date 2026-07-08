class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use dict to count the letter frequency in s.
        cntDict = {}
        for c in s:
            if c in cntDict:
                cntDict[c] += 1
            else:
                cntDict[c] = 1
        # Iterate over t, decrease the frequency by 1
        for c in t:
            if c in cntDict:
                cntDict[c] -= 1
            else:
                return False
        # check if all frequency is 0.
        for cnt in cntDict.values():
            if cnt != 0:
                return False
        return True
        