class Solution:
    """ 

    len # string

    1. extract number up till #
    2. add next number chars after string to res

    """


    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded


    def decode(self, s: str) -> List[str]:
        """
        
              i    
        4#neet4#code4#love3#you

        """
        res = []

        i = 0
        while i < len(s):
            # extract lenth
            length = ""
            while i < len(s) and s[i] != "#":
                length += s[i]
                i += 1
            length = int(length)
            i += 1

            # append string to res
            curr_str = ""
            while length:
                curr_str += s[i]
                i += 1
                length -= 1
            res.append(curr_str)
        
        return res












