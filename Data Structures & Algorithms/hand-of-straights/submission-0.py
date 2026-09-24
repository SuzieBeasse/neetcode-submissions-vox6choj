from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if not n % groupSize == 0:
            return False
        
        freqs = Counter(hand)
        values = sorted(freqs.keys())
        total_groups = n // groupSize

        for i, value in enumerate(values):
            if freqs[value] <= 0:
                continue
            else:
                k = freqs[value]
                for j in range(groupSize):
                    if (value+j) not in freqs or freqs[value+j] < k:
                        return False
                    freqs[value + j] -= k

                total_groups -= k
        return total_groups == 0
        



        