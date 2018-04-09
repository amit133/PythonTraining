#Function without a param
def greetings():
    print('Hello World')

greetings()

#Function with a param
def greetings(name):
    print('Hello {0}'.format(name))

greetings('Amit')

#Function which returns a value
def add(a, b):
    return a + b

a = 2
b = 3
c = add(a, b)

print('{0} + {1} = {2}'.format(a,b,c))
