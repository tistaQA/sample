# List is a datatype that allows multiple values and can be different data types
values = [1, 9, 0, 6, "Rahul", 44, "Rihan"]
print(values[::-1]) # reverse the list
print(values[3:]) # will start from 3rd index nd goes till end
print(values[0])   # 1
print(values[4])   # Rahul
print(values[-1])   # last index value
print(values[2:-1]) # it will print from 2nd index to before last index

values.insert(5, "Shetty")
print(values)

# add a new value at the end
values.append("India")
print(values)

# update
values[2] = 4
print(values)

# delete
del values[3]
print(values)
