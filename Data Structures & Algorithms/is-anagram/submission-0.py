class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = collections.defaultdict(int)
        t_dict = collections.defaultdict(int)
        for c in s:
            s_dict[c] += 1
        for c in t:
            t_dict[c] += 1
        if s_dict != t_dict:
            return False
        return True

        