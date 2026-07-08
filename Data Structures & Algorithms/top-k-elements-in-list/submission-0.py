class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        sortedFreq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sortedFreq][:k]

        