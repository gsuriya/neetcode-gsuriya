class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad_map = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g', 'H', 'I'],
            5: ['J', 'K', 'L'],
            6: ['M', 'N', 'O'],
            7: ['P','Q','R','S'],
            8: ['T','U','V'],
            9: ['W','X','Y','Z']
        }

        ans = []

        if not digits:
            return []

        def dfs(i, path):
            if len(path) == len(digits):
                ans.append(''.join(path))
                return

            for letter in keypad_map[int(digits[i])]:
                path.append(letter.lower())
                dfs(i+1, path)
                path.pop()
        
        dfs(0, [])
        return ans