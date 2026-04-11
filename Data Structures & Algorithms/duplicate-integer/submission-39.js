class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const seen = []
        for (let i = 0; i < nums.length; i++) {
            if (seen.includes(nums[i])) {
                return true
            }
            
            seen.push(nums[i])
        }

        return false
    }
}
