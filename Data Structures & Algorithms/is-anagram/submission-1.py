class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_dict, t_dict = {}, {}
        for l in s:
            s_dict[l] = 1 + s_dict.get(l, 0)
        for l in t:
            t_dict[l] = 1 + t_dict.get(l, 0)
        if s_dict != t_dict:
            return False
        return True