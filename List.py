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
