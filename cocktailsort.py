#Clay Kynor
#11/27/17
#cocktailSort.py - implimentation of cocktailSort.py

from random import randint
from time import time

N = 100 #how many numbers will be sorted

def mySort(A):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0,len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i] #Swaps the numbers that were out of order
                swapped = True
        
    return A

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
    