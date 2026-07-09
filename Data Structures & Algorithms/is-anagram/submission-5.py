class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        from collections import defaultdict
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        
        for c in s:
            count_s[c] += 1
        for c in t:
            count_t[c] += 1
        
        if count_s != count_t:
            return False
        
        return True
        