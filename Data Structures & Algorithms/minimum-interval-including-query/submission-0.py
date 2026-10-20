from heapq import heappush, heappop
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        m = len(intervals)
        if n == 0:
            return
        ans = [-1]*n

        sorted_intervals = sorted(intervals)

        heap_queries = []
        for i, q in enumerate(queries):
            heappush(heap_queries, (q, i))

        heap_int = []
        k = 0
        while heap_queries:
            q, i = heappop(heap_queries)

            while k < m and sorted_intervals[k][0] <= q:
                left, right = sorted_intervals[k]
                length = right - left + 1
                heappush(heap_int, (length, right))
                k += 1

            
            while heap_int and heap_int[0][1] < q:
                heappop(heap_int)

            if heap_int:
                l = heap_int[0][0]
                ans[i] = l
        
        return ans



# Design
# Sort the intervals by smaller left_i
# Create a array ans = [-1]*n
# sort the list of (q[i], i)
# Put intervals in a min heap b
        