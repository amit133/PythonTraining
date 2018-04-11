 
def getAreaOfTriangle(base, height):
    """ Calculate the area of a triangle.

    Area is calculated using the formula: Area = 0.5 * base * height.
    This function throws an assertion error if either base or height is non-positive number
    """
    assert base > 0 and height > 0
    return 0.5 * base * height

if __name__ == "__main__":
    print("Get the area of triangle by providing its base and height")
    try:
        base = float(input("What is the length of the base? "))
        height = float(input("What is the height of triangle w.r.t. base line? "))
    except ValueError as err:
        print('Error: ', err)
        exit(-1);
    
    area = getAreaOfTriangle(base, height)
    print("Area of the triangle with base {0} and height {1} is {2} sq unit: ".format(base, height, area) )
