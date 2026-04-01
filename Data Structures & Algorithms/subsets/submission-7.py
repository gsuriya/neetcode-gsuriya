class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """

        to get all subsets
        - add element
        - dont add element



        """

        res = []

        def dfs(i, path):
            if i == len(nums): # reached end
                res.append(path.copy())
                return
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
            dfs(i+1, path)
        
        dfs(0, [])


        return res
