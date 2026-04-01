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
            while s[j] != "#": # get all digits of string length
                j += 1
            
            s_length = int(s[i:j])
            res.append(s[j+1:j+1+s_length])
            i = j+1+s_length
        
        return res

