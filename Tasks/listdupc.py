numbers = [1, 2, 3, 1,4, 5,3,1,6]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1:
        duplicates.append(num)
print("Duplicate values:", duplicates)
dcount={num: duplicates.count(num) for num in duplicates if duplicates.count(num) > 1}
print("Duplicate counts:", dcount)
