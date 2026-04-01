class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """

        sort - allows skipping duplicates

        use (i+1)
        ~use (never use again, skip all duplicates)

        9 2 2 4 6 1 5

              i
        1 2 2    4 5 6 9

        """
        res = []
        candidates.sort()

        path = []
        def dfs(i, path_sum):
            # ALWAYS PUT SUCCESS BASE CASES FIRST
            if path_sum == target:
                res.append(path.copy())
                return

            if i == len(candidates) or path_sum > target:
                return
            
    
            # use
            path.append(candidates[i])
            dfs(i+1, path_sum + candidates[i])
            path.pop()

            # ~use
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            i += 1
            dfs(i, path_sum)

        dfs(0, 0)
        return res



