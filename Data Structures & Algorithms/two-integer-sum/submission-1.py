class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in _dict:
                return [_dict[diff], i]
            _dict[n] = i

        