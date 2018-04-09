#Dictionary in python: {key:value} pairs

phonebook = {
    "johny": 2233456234
    }

# add a new member to the phonebook
phonebook["john"] = 1234567899
print(phonebook)

# iterate over a dictionary
for name, number in phonebook.items():
    print("phone number of {0} is {1}".format(name, number))

# delete value at specified index using del
del phonebook['john']
print('deleted the phone number of john')
print(phonebook)

phonebook['amiya'] = 4357628934
phonebook['amul'] = 1234576838

print(phonebook)

# delete value at specified index using pop method
phonebook.pop('amiya')
print(phonebook)

# Change the phone number of 'amiya'. Replace the value at index 'amiya'
phonebook['amiya'] = 23234332423423
print(phonebook)
