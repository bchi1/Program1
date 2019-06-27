"""capitalize all the vowels in a string and make
all consonants lower case"""

#First, grabs user string
sentence = input("Please enter a string: ")

#Misc task of setting up dictionary
dictionary = {
    "a" : "A",
    "e" : "E",
    "i" : "I",
    "o" : "O",
    "u" : "U"
}

#Next, converts all letters to lowercase
sentence = sentence.lower()

#Now, iterate through all the vowels, if present in string
#then replace the letter with the capital version
for letter in dictionary:
    if letter in sentence:
        sentence = sentence. replace(letter, dictionary[letter])

#print out the sentence
print(sentence)
