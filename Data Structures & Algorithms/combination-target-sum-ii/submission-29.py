class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """

        9 2 2 4 6 1 5

          i
        1 2 2 4 5 6 9

                []
            [1]    []
        [2]
      [22]   
            

        choose (i+1)
        ~choose (skip all dups)

        """

        candidates.sort()
        res = []
        def dfs(i, path, path_sum):
            if path_sum == target:
                res.append(path.copy())
                return
            
            if i == len(candidates) or path_sum > target:
                return
        
            # choose (i+1)
            path.append(candidates[i])
            dfs(i+1, path, path_sum + candidates[i])
            path.pop()

            # ~choose (skip all dups)
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, path, path_sum)

        dfs(0, [], 0)
        return res



