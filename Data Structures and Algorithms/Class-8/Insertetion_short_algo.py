"""
[4,2,1,5,6]

-> [1,2,4,5,6]
---------------------------------
[Insertion Sort Algorithm]

[22, 12, 15, 3, 4]

-------------
Step - 01:
[12, 22, 15, 3, 4]
-------------
Step - 02:
[12, 15, 22, 3, 4]
-------------
Step - 03:
[12, 15, 3, 22, 4]
-------------
Step - 04:
[12, 15, 3, 4, 22]
"""

# [22, 12, 15, 3, 4]
def insertion_sort_algorithm(lst):
    len_lst = len(lst)

    for index in range(1, len_lst):
        key_value = lst[index]
        previous_index = index - 1

        while previous_index >= 0 and key_value < lst[previous_index]:
            lst[previous_index + 1] = lst[previous_index]
            previous_index -= 1

        lst[previous_index + 1] = key_value

        # [12, 22, 15, 3, 4]
        # [12, 15, 22, 3, 4]

        """
        # [12, 15, 3, 22, 4]
        # [12, 3, 15, 22, 4]
        # [3, 12, 15, 22, 4]
        """

        """
        # [3, 12, 15, 4, 22]
        # [3, 12, 4, 15, 22]
        # [3, 4, 12, 15, 22]
        """
    return lst


lst = [22, 12, 15, 3, 4]
ls = [15,20,25,4,3,2,68,45]
lst = insertion_sort_algorithm(lst)
ls = insertion_sort_algorithm(ls)
print(lst)
print(ls)