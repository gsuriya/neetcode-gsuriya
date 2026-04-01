class Solution {
    /*

    1. create freq_map of nums
    2. bucket sort freq_map.values() - max freq is len(nums)+1
    3. extract values from the end of bucket sort arr
    
    3 3 4 4

                                     i
    bucket_sort = [    [3 4]     [] [] ]
                 f 0 1   2    3  4  5
    */

    topKFrequent(nums, k) {
        // create freq map
        const freq_map = {}
        for (const n of nums) {
            if (!freq_map.hasOwnProperty(n)) {
                freq_map[n] = 0
            }
            freq_map[n] += 1
        }

        // bucket sort - .fill() only works with primitive values
        const bucket_sort = new Array(nums.length+1)
        for (let i = 0; i < bucket_sort.length; i++) {
            bucket_sort[i] = []
        }
        
        for (const [val, freq] of Object.entries(freq_map)) {
            bucket_sort[freq].push(val)
        }

        // extract values from bucket_sort
        const res = []
        let tmp_k = k
        for (let i = bucket_sort.length-1; i >= 0; i--) {
            while (bucket_sort[i].length > 0 && tmp_k > 0) {
                res.push(bucket_sort[i].pop())
                tmp_k -= 1
            }

        }

        return res

    }
}
