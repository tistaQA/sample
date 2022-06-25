try:
    print(x+y)

except:
    print("There is no such variable")

try:
    print(x+y)

except Exception as e:
    print(e)

finally:
    print("Junk data are removed")