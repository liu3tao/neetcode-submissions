class Solution:
    # Create a hash set of unique nums for O(1) look up
    # Go over the set to find start of seq (no n - 1 in the set), into a list
    # Go over the list to find the longest seq
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for n in nums:
            numSet.add(n)
        seqStarts = []
        for n in numSet:
            if n - 1 not in numSet:
                seqStarts.append(n)
        longest = 0
        for n in seqStarts:
            m = n + 1
            while m in numSet:
                m += 1
            longest = max(longest, m - n)
        return longest
        