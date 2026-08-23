class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """

        unique combinations but skip duplicates
        
        sort
        - use (i+1)
        - ~use (skip duplicates)

        curr_sum > target or i at the end --> return

        """

        candidates.sort()
        res = []

        def dfs(i, path, curr_sum):
            if curr_sum == target:
                res.append(path.copy())
                return
            
            if i == len(candidates) or curr_sum > target:
                return
            
            # use (i+1)
            path.append(candidates[i])
            dfs(i+1, path, curr_sum + candidates[i])
            path.pop()

            # ~use (skip dups)
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            i += 1
            dfs(i, path, curr_sum)
        
        dfs(0, [], 0)
        return res





