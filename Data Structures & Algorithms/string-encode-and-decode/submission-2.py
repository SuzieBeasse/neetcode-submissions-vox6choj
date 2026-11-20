class Solution:

    def encode(self, strs: List[str]) -> str:
        curr = ''
        if not strs:
            return ''
        strs.append('')
        for str in strs:
            curr += str
            curr += '---'
        return curr[:-1]

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        strs = s.split('---')
        strs.pop()
        return strs
