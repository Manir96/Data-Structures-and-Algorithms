#num [1,2,3,4,5]
def sumAllNumbers(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sumAllNumbers(lst[1:])

print(sumAllNumbers([2,3,5,8,6,7]))