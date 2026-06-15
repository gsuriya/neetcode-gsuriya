class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
            i
        3 4           ""
                     d   e   f
                    ghi ghi ghi

        path len(digits) --> append to res
        """
        if not digits:
            return []

        digit_to_letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        # generates all combinations for 
        res = []
        def dfs(i, path):
            if i == len(digits): # valid combo
                res.append(''.join(path))
                return
            
            # dfs on every possible letter for this number
            for l in digit_to_letter[digits[i]]:
                path.append(l)
                dfs(i+1, path)
                path.pop()
        
        dfs(0, [])
        return res
