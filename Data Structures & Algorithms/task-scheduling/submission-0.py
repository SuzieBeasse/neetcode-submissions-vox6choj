from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        queue = deque([])

        for key, val in count.items():
            heapq.heappush(heap, (-val, key, 0))
        
        t=0
        while heap or queue:
            #Transfer the cooled tasks from cooling down queue to heap:
            while queue and queue[0][2] <= t:
                (v, k, prev_t) = queue.popleft()
                heapq.heappush(heap, (v, k, prev_t))
            if heap:
                v, k, prev_t = heapq.heappop(heap)
            
                if v < -1:
                    queue.append((v+1, k, t + n + 1))
            t += 1

        return t



    #Available tasks in the heap
    #Cooling tasks in the queue

