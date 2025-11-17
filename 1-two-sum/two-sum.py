class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, a in enumerate(nums):
            if  a in s:
                return [i ,s[a]]
            s[target - a] = i
        return []