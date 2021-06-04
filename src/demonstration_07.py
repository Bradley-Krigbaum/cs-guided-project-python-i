"""
Challenge #7:

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).

Examples:
- nth_smallest([7, 5, 3, 1], 1) ➞ 1
- nth_smallest([1, 3, 5, 7], 3) ➞ 5
- nth_smallest([1, 3, 5, 7], 5) ➞ None
- nth_smallest([7, 3, 5, 1], 2) ➞ 3
"""
def nth_smallest(lst, n):
    if n > len(lst):
        print('that number is too big!!!')
        return None
    if n == 0:
        print("0 isn't an option!")
        return None
    new_lst = lst
    new_lst.sort()
    print(new_lst[n - 1])
    return new_lst[n - 1]



nth_smallest([7, 5, 3, 1], 1)
nth_smallest([1, 3, 5, 7], 3)
nth_smallest([1, 3, 5, 7], 5)
nth_smallest([7, 3, 5, 1], 2)
nth_smallest([7, 3, 5, 1], 0)
