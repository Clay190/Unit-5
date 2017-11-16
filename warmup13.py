#Clay Kynor
#11/16/17
#warmup13.py

from random import randint

words = []

for i in range(1,21):
    num = randint(1,100)
    words.append(num)
   
words.sort()
print(words)
print("The maximum is", words[19])
print("The minimum is", words[0])
print("Sum", sum(words))
