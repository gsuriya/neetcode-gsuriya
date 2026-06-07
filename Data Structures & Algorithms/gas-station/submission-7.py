class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """

        same solution js doing problem here so i leave intutition on first slide

        [-1, -1, 1]

        1. make net_gas arr, curr_sum = 0, start
        2. iterate thru net_gas
        - if curr_sum ever drops negative, then start --> i r all invalid.
        - valid start should be right AFTER i b/c that puts most distance collect more gas
        - until we become negative again at i


        """
        # edge case: its impossible
        if sum(gas) < sum(cost):
            return -1

        # setup
        start = 0
        curr_sum = 0
        net_gas = [gas[i] - cost[i] for i in range(len(gas))]

        for i in range(len(net_gas)):
            curr_sum += net_gas[i]

            # if negative at this point - start --> i don't work
            if curr_sum < 0:
                start = i+1 # put most circular distance to accumulate before coming back to start
                curr_sum = 0

        return start
            