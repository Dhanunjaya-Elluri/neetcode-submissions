class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        def totalH(k, piles):
            total = 0
            for n in piles:
                total += math.ceil(n / k)
            return total

        while l <= r:
            k = l + (r - l) // 2
            if totalH(k, piles) <= h:
                res = min(res, k)
                r = k - 1
            elif totalH(k, piles) > h:
                l = k + 1
        return res
            