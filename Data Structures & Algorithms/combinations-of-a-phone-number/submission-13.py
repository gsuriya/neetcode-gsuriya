class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        0. edge case: if not digits: return []

        hashmap: digit --> list of chars
        1. dfs through each digit
        - create branches for each possible char

        2. if path (possible combo) is length of digits --> res.append(path.copy())

        time: O(n * 4^n)
        space: O(n)

        """

        # edge case
        if not digits:
            return []
        
        # map: digit --> list of possible chars
        digit_map = {
            "2": "ABC",
            "3": "DEF",
            "4": "GHI",
            "5": "JKL",
            "6": "MNO",
            "7": "PQRS",
            "8": "TUV",
            "9": "WXYZ"
        }

        res = []
        
        def dfs(i, path):
            # base case
            if i == len(digits):
                res.append(''.join(path))
                return

            for char in digit_map[digits[i]]: # iterating through possible chars for this digit
                path.append(char.lower())
                dfs(i+1, path)
                path.pop()

        dfs(0, [])
        return res

