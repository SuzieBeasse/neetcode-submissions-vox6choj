from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)

        heap = []

        for i, freq in freqs.items():
            heapq.heappush(heap, (freq, i))
            while len(heap) > k:
                heapq.heappop(heap)

        ans = []
        while heap:
            _, i = heap.pop()
            ans.append(i)
        
        return ans
        