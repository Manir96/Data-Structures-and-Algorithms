
    
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
solution_instance = Solution()
lis = [1,8,6,2,5,4,8,3,7]
mehedi = solution_instance.maxArea(lis)
print(mehedi)