import heapq
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_s = []

    def push(self, val: int) -> None:
        # Appending to the stack
        self.stack.append(val)
        
        if not self.min_s or val <= self.min_s[-1]:
            self.min_s.append(val)
        else:
            self.min_s.append(self.min_s[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_s.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_s[-1]
        
# When popping from stack we need to remove the element from the min stack as well!