class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_s = defaultdict(int)
        for c in s:
            char_s[c] += 1
        
        char_t = defaultdict(int)
        for c in t:
            char_t[c] += 1
        
        if char_s != char_t:
            return False
        
        return True