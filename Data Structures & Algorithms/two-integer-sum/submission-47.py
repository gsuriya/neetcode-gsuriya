class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 

        record numbers:index as you go, if curr number + prev
        one sums to target --> pairing found

        """

        prev_map = {} # num --> i
        
        for i, n in enumerate(nums):
            diff = target - n
            
            # pairing found
            if diff in prev_map:
                return [prev_map[diff], i]

            prev_map[n] = i
        
        return []