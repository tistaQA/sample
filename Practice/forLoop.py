var = [1, 4, 7, "Rahul", 9, 5, "Shetty"]
print(var[-3])
for i in var:
    print(i)

# sum of 1st 6 natural numbers
# range(i,j) means i to j-1

s = 0
for j in range(1, 7):
    s = s + j
print(s)

print("***************************************************************************************************")
# for loop iteration gap will be 3 here
for k in range(2, 12, 3):
    print(k)
print("###################################################################################################")
# range(i) means 0 to i-1
for m in range(10):
    print(m)