"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def quick_sort_by_length(lst):
    prepList = []
    
    for anyString in lst:
        prepList.append( anyString )
    return sorted(prepList)


def sort_by_length( lst ):
    newLst = lst
    
    for i in range( 1, len(newLst) ):
        indexPlaceholder = newLst[i]
        nextValue = i - 1
        
        while nextValue >= 0 and len(indexPlaceholder) < len(newLst[nextValue]):
            newLst[nextValue + 1] = newLst[nextValue]
            nextValue -= 1    
        newLst[nextValue + 1] = indexPlaceholder
    return newLst
