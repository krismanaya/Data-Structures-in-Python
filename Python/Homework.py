import random

## Section 1 ##

## This function returns powers of two up to i. 
def power_of_two(i):
    if not isinstance(i,int): 
        raise TypeError('data must be int type') 
    return [2**k for k in range(0,i)]

#This function returns a random choice from the given range of sequence. 
def choice(data): 
    if not isinstance(data,list): 
        raise TypeError('data must be list type')
    return data[random.randrange(len(data

#This function returns True from a sequence that has at most two distinct numbers.
def distinct_numbers(sequence): 
    if not isinstance(sequence,list): 
        raise TypeError('sequence must be list type')
    for num in sequence: 
        if sequence.count(num) >= 2: 
            return True
        else: 
            return False