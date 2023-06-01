# ok so ill loop over the list of the numbers and save the index
# then ill loop over the list again inside of the first loop
# ill check if the index is not the same and if the number from the first loop plus the number from the second loop are equal to the target
# if it is then ill return the value

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, number in enumerate(nums):
            for index2, number2 in enumerate(nums):
                if number + number2 == target and index != index2:
                    return [index, index2]


# print(Solution().twoSum([2,7,11,15], 9))
# print(Solution().twoSum([3,2,4], 6))
# print(Solution().twoSum([3,3], 6))

# print(Solution().twoSum([3, 3], 6))                  # Output: [0, 1]
# print(Solution().twoSum([2, 5, 7], 12))              # Output: [1, 2]
# print(Solution().twoSum([10, 82, 5], 15))            # Output: [0, 2]
# print(Solution().twoSum([1, 1, 1, 1], 2))            # Output: [0, 1]
# print(Solution().twoSum([-1, -2, -3, -4], -6))       # Output: [1, 3]
# print(Solution().twoSum([0, 1, 2, 3, 4], 6))         # Output: [2, 4]
# print(Solution().twoSum([5, 10, 15, 20], 35))        # Output: [2, 3]
# print(Solution().twoSum([7, 7, 7, 7], 14))           # Output: [0, 1]
# print(Solution().twoSum([1, 2, 3, 4, 5], 8))         # Output: [2, 4]
# print(Solution().twoSum([9, 8, 4, 6, 5], 14))        # Output: [0, 4]
