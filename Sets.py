#Set: Unordered collection of unique values

cars = set(['maruti', 'ford'])
print('car brands: ', cars)

cars.add('tata')

if 'tata' in cars:
    print('new car brand "tata"')

diedCars = frozenset(['ambassador', 'maruti800'])
if 'maruti800' in diedCars:
    print('maruti800 is not produced any more')

## Following statment would give error on execution since it is a frozen set
#diedCars.add('nano')

#operators on set
firstNames = set(['amit','kumar','lalit','shashi', 'avni'])
lastNames = set(['kumar', 'padmanav', 'kashyap'])

sameFirstLast = firstNames & lastNames ## firstNames.intersection(lastNames)
print("These names are used as first or last name", sameFirstLast)

uniqueNames = firstNames | lastNames
print("All unique names: ", uniqueNames)

print( firstNames ^ lastNames)
