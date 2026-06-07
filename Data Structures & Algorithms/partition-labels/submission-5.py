class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """

        all of one letter in one substring

        L       e
        x y x x y z b z b b i s l

        - keep expanding until we get ALL of the letters in curr window
            - if all letters reach, then collapse window and append to res

        1. map letter --> last position in string
        2. sliding window
        - for curr letter, update end w/ last occurence
        - keep expanding until get to end --> append to res and collapse window

        """

        # map letter --> last position in string
        last_i = {}
        for i, c in enumerate(s):
            last_i[c] = i
        
        res = []
        end = 0
        L = 0

        for R in range(len(s)):
            # update end
            end = max(end, last_i[s[R]])
            
            # if at end --> append to res and collapse window
            if R == end:
                res.append(R-L+1)
                L = R+1
                R += 1
        
        return res



