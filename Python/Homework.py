import random

## Section 1 ##
## This function returns powers of two up to i. 
def power_of_two(i): 
    return [2**k for k in range(0,i)]

#This function returns a random choice from the given range of sequence. 
def choice(data): 
    if not isinstance(data,list): 
        raise TypeError('data must be list type')
    return data[random.randrange(len(data))]