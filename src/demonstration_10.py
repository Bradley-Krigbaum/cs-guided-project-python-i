"""
Challenge #10:

Create a function that applies a discount d to every number in the list.

Examples:
- get_discounts([2, 4, 6, 11], "50%") ➞ [1, 2, 3, 5.5]
- get_discounts([10, 20, 40, 80], "75%") ➞ [7.5, 15, 30, 60]
- get_discounts([100], "45%") ➞ [45]

Notes:
- The discount is the percentage of the original price (i.e the discount of
"75%" to 12 would be 9 as opposed to taking off 75% (making 3)).
- There won't be any awkward decimal numbers, only 0.5 to deal with.
"""
def get_discounts(nums, percentage):
    newDecimal = int( percentage.strip('%') ) * .01
    finalPrice = []
    
    for num in nums:
        newNums = num * newDecimal
        finalPrice.append( newNums )
    return finalPrice
    
# get_discounts([2, 4, 6, 8, 10], '50%')
