class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0
        while i < len(s):
            # extract length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # 2
            i = j+1

            # extract word, append to res
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res


