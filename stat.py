#Clay Kynor
#11/15/17
#stat.py - finding stats

numbers = []
while True:
    num = input("Enter a number or press 'q' when finished ")
    if num == 'q':
        break  
    numbers.append(float(num))

numbers.sort()

times = numbers.count()

print("Min: ", min(numbers))
print("Max: ", max(numbers))
print("Mean: ", sum(numbers)//len(numbers))
print("Mode: ")
print("Median: ", numbers[len(numbers)//2,(len(numbers)//2)+1])