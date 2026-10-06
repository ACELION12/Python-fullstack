numbers = [10, 25, 5, 40, 15, 2, 30]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest: #the loop keeps going until it finds out the largest num
        largest = num

    if num < smallest:#same as the largest but for smallest.
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)