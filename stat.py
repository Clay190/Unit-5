#Clay Kynor
#11/15/17
#stat.py - finding stats

numbers = []
while True:
    num = input("Enter a number or press 'q' when finished ")
    if num == 'q':
        break  
    else:
        numbers.append(float(num))

total = 0
for i in range(0, len(numbers)):
    if total<numbers.count(i):
        total = numbers.count(i)

numbers.sort()

print("Min: ", min(numbers))
print("Max: ", max(numbers))
print("Mean: ", sum(numbers)/len(numbers))
print("Mode: ", total)

'''
print("Median: ", numbers[len(numbers)//2,(len(numbers)//2)+1])'''