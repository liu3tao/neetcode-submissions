class Solution:
    def getSignature(self, word: str) -> str:
        letterCnt = [0] * 26
        ordOfA = ord('a')
        for letter in word:
            letterCnt[ord(letter) - ordOfA] += 1
        return ''.join([f'{cnt:02x}' for cnt in letterCnt])

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            signature = self.getSignature(word)
            if signature in groups:
                groups[signature].append(word)
            else:
                groups[signature] = [word]
        return [words for words in groups.values()]
