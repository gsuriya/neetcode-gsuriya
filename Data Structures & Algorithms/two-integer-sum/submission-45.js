class Solution {
    /*
        if theres a prev number that sums to target,
        use that prev number index and curr inddex
    */
    twoSum(nums, target) {
        const prev_map = {} // num --> index
        for (let i = 0; i < nums.length; i++) {
            const complement = target - nums[i]

            if (prev_map.hasOwnProperty(complement)) {  // if num u need in prev_map
                return [prev_map[complement], i]
            }

            prev_map[nums[i]] = i
        }

        return []
    }
}
