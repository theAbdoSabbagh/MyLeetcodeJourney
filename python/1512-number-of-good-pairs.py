class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        placeholder = []
        for item in list(set(nums)):
            k = nums.count(item)
            placeholder.append(k * (k - 1) // 2)
        return sum(placeholder)