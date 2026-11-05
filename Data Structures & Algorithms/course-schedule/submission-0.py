from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numReq = [0] * numCourses
        adj = defaultdict(list)
        
        for a, b in prerequisites:
            adj[b].append(a)
            numReq[a] += 1
        
        queue = deque([])
        studied = 0
      

        for i in range(numCourses):
            if numReq[i] == 0:
                queue.append(i)

        while queue:
            i = queue.popleft()
            studied += 1

            for k in adj[i]:
                numReq[k] -= 1
                if numReq[k] == 0:
                    queue.append(k)
        
        return studied == numCourses
        
        



    

# Design
  # Go through the prereq array and create an adjency map adj[b] = [courses list that require b ]
  # While creating the adj map, keep track of the number of requirements for each course in an array
  # Add all the courses with no requirements to a queue
  # Study, them, and decrement the nr of requirements by 1 for each of the courses in the adj map of each of them
  # Once a course no longer have outstanding req add it to the queue
  #Keep studying while there are courses in the queue
  # Keep track of the number of course studied, if it is equal to numCourses return true else false