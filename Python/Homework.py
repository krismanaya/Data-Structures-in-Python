import random
import math 
import pandas
from collections import Counter


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

## C-1.27: This function is a modified function of factors from page 41 in the book. 
def factors_modify(n): 
    k = 1
    while k*k < n: 
        if n % k == 0:
            yield k
        k += 1
    if k*k == n:
        yield k
    k = k-1
    while k >= 1:
        if n % k == 0:
            yield n // k
        k -= 1
  
## P-2.33        
class Derivative:
    """This class creates a function f and then derives that function 
    using the f(x) method at the bottom """ 
    
    def __init__(self,f,h = 1E-5): 
        self.f = f
        self.h = float(h)
    
    def __call__(self,x): 
        f,h = self.f,self.h
        return (f(x+h)-f(x))/h

def f(x): 
    """this creates the polynomial f for our derivative class."""
    return x

def main():
    """This asks the user to input any polynomial of degree n and 
    then calls the class to return its derivative for the choice of small epsilon."""

    df = Derivative(f)
    x = raw_input("please enter a polynomial: ")
    f(x)
    x = int(input("please enter the input for f(x):"))
    return df(x)


## p-2.34 xs
def split_file():
    """This function takes a document, parses the letters and returns 
    the frequency of the letter in a histogram."""
    l = []
    d = dict()
    with open('p-2.34.txt', 'r') as f: 
        data = f.readlines()
        for line in data: 
            words = line.split()
            for list in words: 
                for letter in list:
                    lower_letter = letter.lower()
                    l.append(lower_letter)
        
    for key in alphabet(): 
        new_value = l.count(key)
        d[key] = new_value
    return d

# l = split_file()
# letter_counts = Counter(l)
# df = pandas.DataFrame.from_dict(letter_counts, orient ='index')
# df.plot(kind='bar')



