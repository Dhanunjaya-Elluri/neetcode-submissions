class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        ar = []
        for n, c in count.items():
            ar.append([c, n])
        ar.sort()
        res = []
        while len(res) < k:
            res.append(ar.pop()[1])
        return res
