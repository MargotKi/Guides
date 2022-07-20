print("Python programming language")
print("Python\nprogramming\nlanguage")
print("Python\"programming\"language")
print("Python\programming\language")

#String variable

sentence = "Python programming language"
print(sentence + " is't difficult")

#Converting strings to Lower and Uppercase

sentence = "Python programming language"
print(sentence.lower())

sentence = "Python programming language"
print(sentence.upper())

#Using Boolean values (lowercase and uppercase)

sentence = "Python programming language"
print(sentence.upper().isupper())

#Counting number of characters in sentence

sentence = "Python programming language"
print(len(sentence))

#Choosing characters from the sentence - The first character is number 0

sentence = "Python programming language"
print(sentence[3])

#Checking the number of chosen character in the text

sentence = "Python programming language"
print(sentence.index("g"))

#Replacing any values by another ones

sentence = "Python programming language"
print(sentence.replace("Python", "Java"))
