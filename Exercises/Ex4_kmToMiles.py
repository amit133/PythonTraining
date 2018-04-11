def convertKmToMiles(km):
    conversionFactor = 0.621371
    miles = conversionFactor * km
    return miles

if __name__ == "__main__":
    print("Welcome to km-to-mile converter program")

    km = float(input("Enter km? "))

    miles = convertKmToMiles(km)
    print("{} km = {} miles".format(km, miles))
