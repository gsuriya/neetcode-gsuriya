class Solution:
    """

    goal: make list of strings into single string

    delimeter: len(s) #
    - basically use len(s) as the separator

    only reason y u hv "#" is b/c len(s) can be more than 2 digits

    

    """

    def encode(self, strs: List[str]) -> str:
        encoded = []
        # for each string, append len(s) + #
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            for c in s:
                encoded.append(c)
        return ''.join(encoded)


    def decode(self, s: str) -> List[str]:
        # take full number (length) up till # for every string

        """
                       j                   
                    i  
        4 # n e e t 4 # c o d e 4 # l o v e 3 # y o u

        """
        decoded = []

        i = 0
        while i < len(s):
            # find length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            i = j+1
            j += length+1

            decoded.append(s[i:j])

            i = j
        
        return decoded






