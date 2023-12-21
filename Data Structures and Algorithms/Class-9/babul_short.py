def bubble_sort(lst):
    len_of_lst = len(lst)

    for outer_index in range(len_of_lst):
        range_of_inner_loop = len_of_lst - outer_index - 1  #

        for inner_index in range(range_of_inner_loop): # 0...1

            print(f"Outer Index {outer_index} and Inner Index {inner_index}")

            if lst[inner_index] > lst[inner_index + 1]:
                temp = lst[inner_index]
                lst[inner_index] = lst[inner_index + 1]
                lst[inner_index + 1] = temp
                # a, b = b, a

            # print(lst)


lst = [-20, 450, 1, 101, -90]  # [-90, -20, 1, 101, 450]
list = [-20,50,-30,7, 450, 1, 101, -90]  
bubble_sort(lst)
bubble_sort(list)

print(lst)
print(list)

"""
1. Syn 
2. Problem Skill 

"""