
#Tuples are immutable

coordinates = (4, 5)

print(coordinates[0])

#if we use tuples we would not just change their values because they are immutable

'''
Basic different between lists and tuples is that we can change values on list but tuples are immutable.
'''

coordinates = [(4, 5), (6,7), (9, 0)]
coordinates[1] = (0, 7)
print(coordinates)