class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.cand = sorted(candidates)
        self.backtrack(target, [], 0, 0)

        return self.ans
    
    def backtrack(self, target: int, curr: list, curr_sum: int, i: int):
        n = len(self.cand)
        if curr_sum == target:
            self.ans.append(curr[:])
            return

        
        for j in range(i, n):
            if j > i and self.cand[j-1] == self.cand[j]:
                continue
            if curr_sum + self.cand[j] > target:
                break

            curr.append(self.cand[j])
            self.backtrack(target, curr, curr_sum + self.cand[j], j+1)
            curr.pop()
            



        