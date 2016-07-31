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

## C-1.19: This function returns the characters of the alphabet in a list.
def alphabet():
    return [chr(letter) for letter in range(97,123)]

## C-1.20: This function shuffles a list of numbers. 
def shuffle(data): 
    return [random.randint(data[0],data[len(data)-1]) for i in range(0,len(data)) if data[i] == data[i]]

## C-1.24: This function returns the number of vowels in a string. 
def count_vowel(str): 
    vowel = 'aeiouAEIOU'
    return sum([str.count(letter) for letter in vowel if letter in str])

## C-1.27: This function is a modified function of factors from page 41 in the book 
def factors_modify(n): 
    k = 1
    list = []
    while k*k < n: 
        if n % k == 0:
            list.append(k)
            list.append(n // k)
            yield list 
            yield list
        k += 1
        if k*k == n:
            list.append(k)
    yield sorted(list)
