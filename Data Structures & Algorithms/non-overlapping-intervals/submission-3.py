class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 1:
            return 0
        intervals_sorted = sorted(intervals)

        ans = 0
        prev_stop = intervals_sorted[0][1]

        for start, stop in intervals_sorted[1:]:
            if start < prev_stop:
                ans += 1
                prev_stop = min(prev_stop, stop)
            else:
                prev_stop = stop
        
        return ans
        
