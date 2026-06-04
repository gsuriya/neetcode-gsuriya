class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """

        neetcode way:
        - tracking last position of each character

        1. map char --> last position of char
        2. iterate thru s
        - for char[i], find last position of it in the string --> from i to last position is window
        - as we iterate through this window, we may find MORE characters which have a LATER last occurence
        - so update the last occurence even FARTHER --> once we hit the end, now we know we have ALL of
          the characters in our partition (like all the x's and y's in the string) so we can append to res

              
        L       R
        x y x x y z b z b b i s l

        """

        # map char --> last position in string
        last_indices = {}
        for i, c in enumerate(s):
            last_indices[c] = i
        
        # for char currently on, update "end" 
        res = []
        R = 0
        L = 0
        for i, c in enumerate(s):
            R = max(R, last_indices[c])

            # all of values collected, new window
            if i == R:
                res.append(R-L+1)
                R += 1
                L = R

        return res
