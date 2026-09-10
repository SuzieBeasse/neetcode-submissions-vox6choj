class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        o = []
        star = []

        for i in range(n):
            c = s[i]
            if c == '(':
                o.append(i)
            elif c == '*':
                star.append(i)
            else:
                if not o and not star:
                    return False
                if len(o) > 0:
                    o.pop()
                else:
                    star.pop()
        
        while o and star and o[-1] < star[-1]:
            o.pop()
            star.pop()

        return len(o) == 0
            
        