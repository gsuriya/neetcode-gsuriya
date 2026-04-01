class Solution:
    """

    can't join on delimeter b/c strings can hv the delimeter in them

    [Hello, World]

           i
    5#Hello5#World

    """

    def encode(self, strs: List[str]) -> str:
        # format: length#string
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        # get length up to delimter (#)
        res = []

        i = 0
        while i < len(s):
            # length up till delimeter
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1
            length = int(length)
            i += 1
            
            tmp = ''
            while i < len(s) and length:
                tmp += s[i]
                length -= 1
                i += 1
            res.append(tmp)
        
        return res
                


            


