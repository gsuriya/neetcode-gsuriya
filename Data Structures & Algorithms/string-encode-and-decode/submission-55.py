class Solution:
    """

    length # string

    [bob, jeff]

     
         i  
    3#bob4#jeff    

    """
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
            length = int(s[i:j])

            # extract actual string
            i = j+1
            res.append(s[i:i+length])
            i += length

        return res

