"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt):
    newString = txt
    xNums = 0
    
    for i in newString:
        if i == 'x' or i == 'X':
            xNums += 1
            print( xNums )
            
    if xNums >= ( len(newString) - xNums ):
        return True
    elif xNums == 0:
        return True
    elif xNums < ( len(newString) - xNums ):
        return False
        
        
        
