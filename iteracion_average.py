#find the average in seirie of numbers
count = 0
sum = 0
print("Before", count, sum)
for value in [9, 41, 12, 3, 64, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, float(sum/count))