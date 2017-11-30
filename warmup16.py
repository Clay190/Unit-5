#Clay Kynor
#11/30/17
#warmup16.py - Write a function that takes a list of numbers as an argument and returns another list where each number is doubled

def double(L):
    N = []
    for i in L:
        N.append(i*2)
    return N
        
print(double([1,3,6,12,33]))
