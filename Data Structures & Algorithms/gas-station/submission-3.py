class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        start = 0

        for i in range(n):
            if tank < 0:
                start = i
                tank = 0
            tank += gas[i] - cost[i]
        
        return start

        





    
    # Design
    # Start at the gas station with the most gas. Go through the gas station from there. If you can make the loop it works.
    # What about calculating the gas - cost 