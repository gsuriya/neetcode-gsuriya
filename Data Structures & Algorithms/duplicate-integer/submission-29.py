class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bucket = set()

        for number in nums:
            # check if this number is already in the bucket
            if number in bucket:
                return True # there are duplicates
            
            bucket.add(number)

        return False