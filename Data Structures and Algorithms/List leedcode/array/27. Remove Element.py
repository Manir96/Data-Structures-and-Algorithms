
class Solution(object):
    def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        
        return len(nums)

# class solution(object):
#     def removeElement(nums, val):
        
#         k=0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k += 1
#             return k

    # Example 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = removeElement(nums1, val1)
    print("Output:", k1, "nums:", nums1[:k1])

    # Example 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = removeElement(nums2, val2)
    print("Output:", k2, "nums:", nums2[:k2])