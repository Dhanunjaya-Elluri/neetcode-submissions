class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {} # val -> index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dict_:
                return [dict_[diff], i]
            dict_[num] = i


        