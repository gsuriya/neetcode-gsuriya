class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """

        problem:
        - duplicates in input array
        - use each elem once
        - HOWEVER, no duplicate combos (sets)

        solution:
        - sort()
        - use (i+1), each num only one time
        - ~use (skip all i's), only distinct branches (one 1, two 1, three, 1)

        """

        res = []
        candidates.sort()

        def dfs(i, path, path_sum):
            if path_sum == target:
                res.append(path.copy())
                return
            if i == len(candidates) or path_sum > target:
                return
            
            # use (i+1)
            path.append(candidates[i])
            dfs(i+1, path, path_sum + candidates[i])
            path.pop()

            # ~use (skip all)
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, path, path_sum)
        
        dfs(0, [], 0)
        return res