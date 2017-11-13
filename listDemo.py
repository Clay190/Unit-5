#Clay Kynor
#11/13/17
#listDemo.py - print out first and last words in list

words = input('Enter some words: ').split(' ')

#print out list one item for line

for w in words:
    print(w)
    
print('The first word was', words[0])
print('The last word was', words[-1])