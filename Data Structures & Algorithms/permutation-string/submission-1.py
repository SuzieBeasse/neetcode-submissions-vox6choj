from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1 = Counter(s1)

        curr = dict()
        left, right = 0, 0

        while left <= right < len(s2):
            c = s2[right]
            if c not in count_s1:
                curr = dict()
                right += 1
                left = right
            
            else:
                curr[c] = curr.get(c, 0) + 1
                if right - left +1 == len(s1):
                    if curr == count_s1:
                        return True
                   
                    curr[s2[left]] -= 1
                    left += 1
                right +=1
        return False
            
            



        