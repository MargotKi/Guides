
#List functions

#now programm prints the shopping list and additionally to do list

to_do = ["clean bathroom", "take a bath"]
shopping = ["Apples", "Bananas", "Plums", "Milk", "Ice cream"]
shopping.extend(to_do)
print(shopping)


#now the programm will print not only the shopping listr but aditionally tings in breakets

to_do = ["clean bathroom", "take a bath"]
shopping = ["Apples", "Bananas", "Plums", "Milk", "Ice cream"]
shopping.append("Bread")
print(shopping)


#now the programm will print not only the shopping listr but aditionally pushed the rest things

to_do = ["clean bathroom", "take a bath"]
shopping = ["Apples", "Bananas", "Plums", "Milk", "Ice cream"]
shopping.insert(2, "Yoghurt")
print(shopping)


#now the programm is printing all shopping list except this which we removed

to_do = ["clean bathroom", "take a bath"]
shopping = ["Apples", "Bananas", "Plums", "Milk", "Ice cream"]
shopping.remove("Plums")
print(shopping)


#now the programm pops the last element from the list

to_do = ["clean bathroom", "take a bath"]
shopping = ["Apples", "Bananas", "Plums", "Milk", "Ice cream"]
shopping.pop()
print(shopping)


# shows us on which possition is that thing in the list

to_do = ["clean bathroom", "take a bath"]
shopping = ["Apples", "Bananas", "Plums", "Milk", "Ice cream"]

print(shopping.index("Milk"))


#Programm counts how many timet this thing was on the list

to_do = ["clean bathroom", "take a bath"]
shopping = ["Apples", "Milk", "Bananas", "Plums", "Milk", "Ice cream"]

print(shopping.count("Milk"))


#programm sorts things from list in arranged alphabetically

to_do = ["clean bathroom", "take a bath"]
favourite_num = [1, 3, 7, 9, 5, 32, 2040]
shopping = ["Apples", "Milk", "Bananas", "Plums", "Milk", "Ice cream"]
shopping.sort()
favourite_num.sort()
print(shopping)
print(favourite_num)


#programm reveses order of the list

to_do = ["clean bathroom", "take a bath"]
favourite_num = [1, 3, 7, 9, 5, 32, 2040]
shopping = ["Apples", "Milk", "Bananas", "Plums", "Milk", "Ice cream"]
shopping.reverse()
print(shopping)


#We can copy the list

to_do = ["clean bathroom", "take a bath"]
favourite_num = [1, 3, 7, 9, 5, 32, 2040]
shopping = ["Apples", "Milk", "Bananas", "Plums", "Milk", "Ice cream"]

shopping_v2 = shopping.copy()

print(shopping_v2)