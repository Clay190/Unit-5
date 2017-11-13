#Clay Kynor
#11/13/17
#middleWord.py - finds the middle word

words = input('Enter a list of words: ').split(' ')
length = (len(words))
if length%2==0:
    print("The middle word(s): ", words[(length//2-1):((length//2+1))])
else:
    print("The middle word(s): ", words[(length//2)])