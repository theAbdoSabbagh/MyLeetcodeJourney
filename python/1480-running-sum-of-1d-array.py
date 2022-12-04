class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new = []
        for index, item in enumerate(nums, start=1):
            new.append(sum(nums[:index]))
        return new