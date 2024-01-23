class Solution(object):
    def twoSum(self, nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    return [i, j]
        return []
# Example 1
nums1 = [2, 7, 11, 15]
target1 = 9
sol = Solution()
print(sol.twoSum(nums1, target1))  # Output: [0, 1]

# Example 2
nums2 = [3, 2, 4]
target2 = 6
print(sol.twoSum(nums2, target2))  # Output: [1, 2]

# Example 3
nums3 = [3, 3]
target3 = 6
print(sol.twoSum(nums3, target3))  # Output: [0, 1]

nums4 = [2,4,6,7,8,10]
target4 = 6
print(sol.twoSum(nums4, target4))