class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        this problem is easy as shit codewise, all intuition
        and its easy intuition at that too

        1. think of a net_gas arr instead where u can only 
           move to next node if net_gas[i] is positive
        2. use this net_gas arr as mental model:

                start      i
        net_gas = [3, 2, -10, 12]

        curr_sum = 3 + 2 + (-10) = -5
        @ i, we can't move to the next node so we "failed"

IMPORTANT: all the indices from start -> i are NOT valid starts
           - starting @ start lead to negative so start is out
           - the middle indices have LESS accumulated gas than if
             we started @ start, so curr_sum will be even more 
             negative at i
           - i+1 index (the 12) has the highest chance of being 
             the valid start b/c it gives the MOST TIME to 
             accumulate gas before coming back to i. it is the
             FARTHEST away from i in terms of distance and time
             to accumulate gas.
           - so we assume i+1 is the next valid start since its
             farthest away from the fail point

        btw only impossible to travel around if 
        sum(gas) < sum(cost)

        theres a solution if 
        sum(gas) >= sum(cost) --> u can move through the entire net_diff
                                  arry somehow

        """
        # no solution edge case
        if sum(gas) < sum(cost):
            return -1

        # create net_diff array
        net_diff = [0] * len(gas)
        for i in range(len(gas)):
            net_diff[i] = gas[i] - cost[i]
        
        """
           S
           i
        -1 0 -1 3

        """

        # greedy on net_diff array
        start = 0
        curr_sum = 0 # curr_sum FROM START
        i = 0
        while i < len(net_diff):
            curr_sum += net_diff[i]

            # fails --> move start to i+1
            if curr_sum < 0:
                start = i+1
                curr_sum = 0

            i += 1

        return start
