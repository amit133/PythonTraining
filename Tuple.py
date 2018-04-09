#Tuples: Immutable group of values
tup = ('physics', 'chemistry', 1997, 2000);

print(tup)

if isinstance (tup, tuple):
    print("It is a tuple")

print ("tup[2]: ", tup[2])
print ("tup[1:3]", tup[1:3])
print ("tup[1:]", tup[1:])

#delete tuple
del tup

#Trying to print a deleted tuple object would cause an error
# NameError: name 'tup' is not defined
print(tup)
