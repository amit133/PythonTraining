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
