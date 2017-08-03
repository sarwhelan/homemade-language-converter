# -*- coding: utf-8 -*-

wordz = raw_input("enter the sentence you want to translate: ")
print("normal boring english: ", wordz)

coolerWords = "cooler: "

for letter in wordz:
    if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
        coolerWords += letter.upper() + " "
    elif(letter == ' '):
        coolerWords += " 👏🏼  "
    else:
        coolerWords += letter.upper() + "op "

print(coolerWords)
