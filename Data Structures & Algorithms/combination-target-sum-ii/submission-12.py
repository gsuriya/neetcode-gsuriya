class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        candidates.sort()

        def dfs(i, path, path_sum):
            if path_sum == target:
                ans.append(path.copy())
                return
            
            if path_sum > target or i == len(candidates):
                return
            
            # include candidates[i]
            path.append(candidates[i])
            dfs(i+1, path, path_sum + candidates[i])
            path.pop()

            # skip candidates[i] and duplicates
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, path, path_sum)

        dfs(0, [], 0)
        return ans