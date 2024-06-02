from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for k in range(len(nums)):
                if k != i:
                    if nums[i] + nums[k] == target:
                        return i, k
