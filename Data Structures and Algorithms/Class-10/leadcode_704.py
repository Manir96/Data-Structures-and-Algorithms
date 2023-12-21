"""
1. Sorted
lst = [10, 20, 20, 30, 50]
value = 50

isExist ? True : False
---------------------------------
[10, 20, 30, 40, 50, 60]

len = 5
start = 0
end = 4
mid = (0+4)/2 = 2
---
1. mid == value ? [30]
start = mid + 1 = 2 + 1 = 3
end = 4
mid = 3 + 4 / 2 = 3

2. mid== value | 100 == 40

start = 4
end = 4
mid = 4 + 4  / 2 = 4

mid == value ? 50 == 50 ? true

start = 5
end = 5

2.5 -> 2
"""


def search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:

        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1

    return -1


lst = [10, 20, 30, 40, 50, 60]
target = 50
print(search(lst, target))