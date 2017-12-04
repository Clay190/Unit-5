#Clay Kynor
#12/4/17
#quiz5.py - Unit Quiz

from random import randint

def rand5():
    nums = []
    for i in range(0,5):
        nums.append(randint(1,100))
    return nums
        
def lastElement(L):
    word = (L[-1])
    return word 
    
def wordLengths(W):
    words = []
    for word in W:
        words.append(len(word))
    return words
    
def biggest(N):
    total = 0
    for num in N:
        if num>total:
            total = num
    return total
        
print(rand5())
print(lastElement(['cat','dog','rat']))
print(wordLengths(['the','cat','is','hungry']))
print(biggest([3,-1,5,-2,7,2,1]))