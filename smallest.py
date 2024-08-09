#the code find the smallest number
smallest = None
print("Before")
for value in [9, 23, 18, 3, 72, 94] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print("After", smallest)