file = open("test.txt")
print(file.read()) # read all the characters of file

print(file.read(5)) # read n number of characters by passing parameter

# read one single line at a time
print(file.readline())

print(file.readline())


file.close()

