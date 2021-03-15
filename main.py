'''
CECS 229

Lab2: Find all of the positive divisors of a positive integer from its prime factorization

Algo: add 1 and number to the list
then multiply all prime factorications once with each other
then divide given number by the current numbers in the list and add the num if it is a hole numbers\
sort list and delete duplicates

'''

def findDivisors( nums ):
    finalNum = 1
    for x in nums:
        finalNum *= x
    return finalNum


nums = [1,2,3]
print(findDivisors( nums ))


