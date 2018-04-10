import cmath

# This function solves a quadratic equation
# ax2 + bx + c = 0
def solveQuadEqu(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant == 0:
        alpha = -b/(2*a)
        print("There is one solution for this quadratic equation: ", alpha)
    elif discriminant > 0:
        delta = discriminant ** 0.5
        alpha = (-b + delta)/(2*a)
        beta = (-b - delta)/(2*a)
        print("There are two solutions for the quadratic equation: {0} and {1}".format(alpha, beta))
    else:
        #print("Negative discriminant")
        delta = cmath.sqrt(discriminant)
        alpha = (-b - cmath.sqrt(discriminant))/(2*a)
        beta = (-b + cmath.sqrt(discriminant))/(2*a)
        print("There are two solutions for the quadratic equation: {0} and {1}".format(alpha, beta))
    

if __name__ == "__main__":
    print("Welcome to the solver of quadratic equation of the form ax2+bx+c=0")
    a = int(input("Please provide a: "))
    b = int(input("Please provide b: "))
    c = int(input("Please provide c: "))
    #print(type(a), type(b), type(c))

    solveQuadEqu(a, b, c)
