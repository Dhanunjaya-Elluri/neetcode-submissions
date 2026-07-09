class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            k = [0] * 26
            for c in s:
                k[ord(c) - ord('a')] += 1
            key = tuple(k)
            if key not in res:
                res[key] = []
            res[key].append(s)
        return list(res.values())