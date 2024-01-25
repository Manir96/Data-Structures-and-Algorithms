class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        simo = set(nums)
        diy = {}
        for i in simo:
            diy[i] = nums.count(i)

        max_value = max(diy.values())
        sum1 = 0
        for i in diy.keys():
            if diy[i] == max_value:
                sum1 += diy[i]

        return sum1

solution_instance = Solution()
nums = [1, 2, 2, 3, 3, 4, 5]

result = solution_instance.maxFrequencyElements(nums)
print(result)