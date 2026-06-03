class Solution:
    def mySqrt(self, x: int) -> int:
        # 1, 2, 3, 4, 5, 6, 7, 8, 9 #x = 9
        # l = 1, r = 9, m = 5, m2 = 25 > x
        # l = 1, r = 4, m = 2, m2 = 4 < x
        # l = 3, r = 4, m = 3, m2 = 9 == x, return m

        # 1, 2, 3, 4, 5, 6, 7, 8, 9 #x = 8, res = 0
        # l = 1, r = 9, m = 5, m2 = 25 > x
        # l = 1, r = 4, m = 2, m2 = 4 < x, res = 2
        # l = 3, r = 4, m = 3, m2 = 9 > x,
        # l = 3, r = 3, m = 3, m2 = 9, return res=2
        l, r = 0, x
        res = 0
        while l <= r:
            mid = l + ((r-l)//2)
            if mid ** 2 > x:
                r = mid - 1
            elif mid ** 2 < x:
                l = mid + 1
                res = mid
            else:
                return mid
        return res
        