class Solution {
    /**
     * prev_map # num --> i
     * 
     * if curr + smth in prev = target, then return indices
     */
    twoSum(nums, target) {
        const prev_map = {}

        for (let i = 0; i < nums.length; i++) {
            const complement = target - nums[i]

            if (prev_map.hasOwnProperty(complement)) {
                return [prev_map[complement], i]
            }

            prev_map[nums[i]] = i
        }

        return []

    }
}
