"""
[1,2,3,4,5,6,7] # Sorted / Unsorted

value = 5 -> is Exist ? True : False

1 sec ? 1000 Sec
"""

def linear_search(lst, value):
    for num in lst:
        if num == value:
            return True

    return False


lst = [2, 10, 3, 6, 1, 8]
value = 3  # 10 - True
print(linear_search(lst, value))