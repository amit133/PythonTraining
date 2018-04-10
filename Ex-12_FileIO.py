## Read operations
fh = open("tuple.py")

## Read all the lines in the file using a for loop
for line in fh:
    print(line)

## Read all the lines in the file at once
print (fh.read())

## Read one line at a time
print(fh.readline())

## Read a list of lines, all content of a file in just a single line
print(fh.readlines())

## close the file
fh.close()


### Write operations
fh = open("hello.txt", "w")

## A list of strings
linesOfText = ["This is a new line",
               "This is 2nd line",
               "This is another new line"]

## Write a new line with a line feed at the end of it
fh.writelines(line + '\n' for line in linesOfText)

## Following way of writing each string on a new line doesn't add a '\n' after the last string
fh.write('\n'.join(linesOfText))
fh.write('\n')
fh.close()

fh = open("hello.txt", "a")
fh.write("hello there\n");
fh.write("Is this on a new line\n")
fh.close()
