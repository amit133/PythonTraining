# variable types
myint = 2
print(myint)

myfloat = 2.1
print(myfloat)

mystr1 = 'string under single quote'
print(mystr1)

mystr2 = "string under double quote"
print(mystr2)

print('{1} {0}'.format('one', 'two'))

#Operators
squared = 5 ** 2
print('square of 5 is {0}'.format(squared))

helloworld = 'hello' + " " + 'world'
print('{}\n'.format(helloworld))

manyhellos = 'hello' * 5
print(manyhellos)

#Lists
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings = []
strings.append('hello')
strings.append('world')

names = ["John", "Eric", "Jessica"]

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

even_nums = [2,4,6]
odd_nums = [1,3,5]
all_nums = odd_nums + even_nums
print(all_nums)

repeatlist = even_nums * 2
print(repeatlist)


#Strings
name = "John"
age = 23
print("{0} is {1} years old.".format(name, age))

astring = "hello world"
splitList = astring.split(" ")
print(splitList)

s = "Strings are awesome!"
print("Lenght of s = %d" % len(s))
print("Lenght of s = {}".format(len(s)))

if(s.startswith("Str")):
    print("Good string")

if(s.endswith("me!")):
    print("End of string")

#Reverse the string
print(s[::-1])

#Print chars at odd locations
print(s[1::2])

print(s.upper())
print(s)

#Decision making
if True:
    print ("hard coded True")

if (True):
    print("Bracketed if")

name = ['amit', 'kumar']
fname = 'amit'
if fname in name:
    print("You are '{0} {1}'".format(name[0], name[1]))

#Loop
primes = [2,3,5,7]
for prime in primes:
    print(prime, end=' ')

print()

counter = 0
while counter < len(primes):
    print(primes[counter], end=' ')
    counter += 1;
else:
    print("\nAll list elements printed")
