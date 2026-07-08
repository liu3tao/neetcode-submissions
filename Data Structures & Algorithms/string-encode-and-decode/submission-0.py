import io

class Solution:
    # 1 leading byte as the length of the str + leading byte.
    def encode(self, strs: List[str]) -> str:
        builder = io.StringIO()
        for s in strs:
            leadingChar = chr(len(s) + 1)
            builder.write(leadingChar)
            builder.write(s)
        return builder.getvalue()

    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        while idx < len(s):
            strLen = ord(s[idx])
            res.append(s[idx + 1: strLen + idx])
            idx += strLen
        return res

