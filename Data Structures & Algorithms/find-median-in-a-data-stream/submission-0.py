import heapq
class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []
        self.n = 0


    def addNum(self, num: int) -> None:
        if self.n == 0:
            self.n += 1
            heapq.heappush(self.lower, -num)
            return
        # Add num to the correct heap
        if num <= -1 * self.lower[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)
        
        # Make sure we have the correct len in both heap
        while len(self.lower) > len(self.upper)+1:
            curr = heapq.heappop(self.lower)
            heapq.heappush(self.upper, -curr)
        
        while len(self.upper) > len(self.lower):
            curr = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -curr)

        # Track the number of elements seen so far
        self.n += 1
        
    def findMedian(self) -> float:
        if self.n % 2 == 0:
            med = (self.upper[0] - self.lower[0]) / 2

        else:
            med = -self.lower[0]
        return float(med)
        

# Design:
# Lower is a max heap
# Upper is a min heap
# Adding a num: either num <= -1 * lower[0] or num >=