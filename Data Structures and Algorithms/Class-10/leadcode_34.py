"""
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""


class Solution(object):
    def searchRange(self, nums, target):
        lenOfNums = len(nums)

        start = 0
        end = lenOfNums - 1
        isExist = self.search(nums, target)

        if isExist:
            for index in range(0, lenOfNums):

                if nums[start] == nums[end]:
                    return [start, end]
                elif nums[start] < target:
                    start += 1
                else:
                    end -= 1

        else:
            return [-1, -1]

    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1

        return False

nums = [2,3,3,3,5,6,7,8,9,10]
target = 2-9
solution = Solution()
print(solution.searchRange(nums, target))
