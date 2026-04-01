class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
                  "" 
            d      e      f
          g h i  g h i  g h i

        i
        3 4

        """
        if not digits:
            return []

        digit_to_char = {
            "2": ['a', 'b', 'c'],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []

        path = []
        def dfs(i):
            if i == len(digits):
                res.append(''.join(path.copy()))
                return
            
            for c in digit_to_char[digits[i]]:
                path.append(c)
                dfs(i+1)
                path.pop()
        
        dfs(0)
        return res

