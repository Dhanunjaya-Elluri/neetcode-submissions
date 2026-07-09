class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {} # k: n, v: i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dict_:
                return [dict_[diff], i]
            dict_[n] = i
        return -1
        