import random

## Section 1 ##

## R-1.11: This function returns powers of two up to i. 
def power_of_two(i):
    return [2**k for k in range(0,i)]

## R-1.12: This function returns a random choice from the given range of sequence. 
def choice(data): 
    return data[random.randrange(len(data))]

## C-1.15: This function returns True from a sequence that has at most two distinct numbers.
def distinct_numbers(sequence): 
    for num in sequence: 
        if sequence.count(num) >= 2: 
            return False
    return True  

#T# C-1.19: This function returns the characters of the alphabet in a list.
def alphabet():
    str = 'abcdefghijklmnopqrstuvwxyz'
    return [letter for letter in str]