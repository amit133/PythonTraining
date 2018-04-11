def swap(num1, num2):
    num1,num2=num2,num1
    return num1,num2

if __name__ == "__main__":
    print("Swap two given integer numbers using this program")

    #num1 = int(input("What is the first number? "))
    #num2 = int(input("What is the second number? "))

    ## swap by the simple assignment method
    #num1,num2 = num2,num1
    #num1,num2 = swap(num1,num2)
    #print("Numbers after swapping are {} {}".format(num1, num2))

    ## Take a list of numbers as input
    num_to_swap = input("Enter two numbers, separated by space, to swap: ")
    print(type(num_to_swap))

    ## Following code gives error: int() can't take a generator
    ##num1,num2 = int(num for num in num_to_swap)
    nums = num_to_swap.split()
    print(type(nums))

    if len(nums) != 2:
        print("Enter two and only two numbers")
        exit();
        
    num1,num2 = nums[0], nums[1]
    #num1,num2 = num_to_swap.split()
    print(num1, type(num1))
    print(num2, type(num2))

    num1,num2 = swap(int(num1), int(num2))
    print("Numbers after swapping are {} {}".format(num1, num2))
