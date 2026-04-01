class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 # keep incrementing j until "#" found
            
            # "#" found, get integer
            res.append(s[j+1:j+1+int(s[i:j])])
            i = j + int(s[i:j]) + 1
        
        return res
            
