#Clay Kynor
#11/15/17
#dictionaryDemo.py - list practice

dictionary = ['alphabet','sweatshirt','sweatpants','shorts','computer','waterbottle']

dictionary.sort()

number = int(input("what number word would you like to look up?"))
if number >len(dictionary):
    print("Bruh, you stupid")
else:
    print("Word number", number, "is", dictionary[number-1])
