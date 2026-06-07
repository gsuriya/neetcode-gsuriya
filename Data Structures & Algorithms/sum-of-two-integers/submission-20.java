class Solution {
    public int getSum(int a, int b) {
        /*

        trick:
        1. a = a ^ b
        2. b (carry) = (a & b) << 1

        if b != 0: repeat and eventually a will be final sum

        */

        while (b != 0) { // while carry != 0
            int sum = a ^ b;
            int carry = (a & b) << 1;

            a = sum;
            b = carry;
        }

        return a;

    }
}



