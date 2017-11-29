#Clay Kynor
#11/29/17
#insertionSort.py - making a sorting algorithm

from random import randint
from time import time

N = 100 #how many numbers will be sorted

'''
procedure bubbleSort( A : list of sortable items )
    n = length(A)
    repeat 
        swapped = false
        for i = 1 to n-1 inclusive do
            /* if this pair is out of order */
            if A[i-1] > A[i] then
                /* swap them and remember something changed */
                swap( A[i-1], A[i] )
                swapped = true
            end if
        end for
    until not swapped
end procedure'''

def mySort(L):
    swapped = True
    while swapped == True:
        for i in range(1,N):
            if L[i-1] > L[i]:
                A[i], A[i+1] = A[i+1], A[i]
        swapped = False
    return L

if __name__ == '__main__':
    
    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
        
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    t2 = time()
       
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
    
