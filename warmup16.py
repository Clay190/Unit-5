#Clay Kynor
#11/30/17
#warmup16.py - Write a function that takes a list of numbers as an argument and returns another list where each number is doubled



def double():
    L = [1,3,6,12,33]
    num = len(L)
    for i in range(0,num):
        L[i] = L[i]*2
    return L
        
print(double())
