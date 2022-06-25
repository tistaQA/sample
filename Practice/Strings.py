str = "RahulShetty.com"

str1 = "Consulting firm"
str2 = 100
str3 = "Rahul"
print(str[0])  # R

print(str[0:5])  # Rahul  # if you want substring in python
print(str, str1, str2)  # concatenation

# whether str3 presents in str or not i.e substring check in python
print(str3 in str)

# split and extract in python
var = str.split("c")
print(var)
print(var[1])

# trim (removing space before and after)
str4 = " University "
print(str4.strip())

# removing left white space
print(str4.lstrip())

# removing right white space
print(str4.rstrip())
