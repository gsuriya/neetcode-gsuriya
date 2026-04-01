class Solution {
    /*

    seen list
    push to list as we seen numbers

    */
    hasDuplicate(nums) {
        const seen = [];

        for (const n of nums) {
            if (seen.includes(n)) {
                return true;
            }

            seen.push(n);
        }

        return false;
    }
}
