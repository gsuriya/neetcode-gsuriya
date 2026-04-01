class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (s + "3840")
        return res

    def decode(self, s: str) -> List[str]:
        # you can only decode what was encoded
        res = s.split("3840")
        res.pop()
        return res